from dataclasses import dataclass
from typing import List
from typing import Union

import numpy as np

from sonusai.mixture.mixdb import Mixture
from sonusai.mixture.mixdb import MixtureDatabase

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = dict()


def build_noise_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[List[np.ndarray]]:
    """Build a database of noise audio data."""
    from tqdm import tqdm

    from sonusai.mixture import apply_augmentation

    noise_audios = list()
    for file_index in tqdm(range(len(mixdb.noises)), desc='Read noise audio', disable=not show_progress):
        audio_in = read_audio(name=mixdb.noises[file_index].name)
        noise_audios.append(list())
        for augmentation_index, augmentation in enumerate(mixdb.noise_augmentations):
            noise_audios[-1].append(apply_augmentation(audio_in=audio_in, augmentation=augmentation))

    return noise_audios


def build_target_audios(mixdb: MixtureDatabase, show_progress: bool = False) -> List[np.ndarray]:
    """Build a list of target audio data."""
    from tqdm import tqdm

    from sonusai.mixture import MixtureDatabase
    from sonusai.utils import p_tqdm_map

    MP_DICT['mixdb']: MixtureDatabase = mixdb

    indices = list(range(len(mixdb.targets)))
    progress = tqdm(total=len(indices), desc='Read target audio', disable=not show_progress)
    target_audios = p_tqdm_map(_read_target_audio, indices, progress=progress)
    return target_audios


def _read_target_audio(file_index: int) -> np.ndarray:
    """Parallel target audio reader kernel."""
    mixdb: MixtureDatabase = MP_DICT['mixdb']
    return read_audio(name=mixdb.targets[file_index].name)


def check_audio_files_exist(mixdb: MixtureDatabase) -> None:
    """Walk through all the noise and target audio files in a mixture database ensuring that they exist."""
    from os.path import exists

    from sonusai import SonusAIError
    from sonusai.mixture import tokenized_expandvars

    for file_index in range(len(mixdb.noises)):
        file_name, _ = tokenized_expandvars(mixdb.noises[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')

    for file_index in range(len(mixdb.targets)):
        file_name, _ = tokenized_expandvars(mixdb.targets[file_index].name)
        if not exists(file_name):
            raise SonusAIError(f'Could not find {file_name}')


def read_raw_target_audio(mixdb: MixtureDatabase,
                          show_progress: bool = False) -> List[np.ndarray]:
    """Read in all audio data beforehand to avoid reading it multiple times in a loop."""

    from tqdm import tqdm

    from sonusai.utils import p_tqdm_map

    names = [target.name for target in mixdb.targets]
    progress = tqdm(total=len(names), desc='Read target audio', disable=not show_progress)
    raw_target_audio = p_tqdm_map(read_audio, names, progress=progress)
    progress.close()

    return raw_target_audio


def get_target_noise_audio(mixdb: MixtureDatabase,
                           mixture: Mixture,
                           raw_target_audios: List[np.ndarray],
                           raw_noise_audios: List[List[np.ndarray]]) -> (List[np.ndarray], np.ndarray):
    """Apply augmentations and return augmented target and noise data."""

    from sonusai import SonusAIError
    from sonusai.mixture import apply_augmentation

    target_file_index = mixture.target_file_index
    target_augmentation_index = mixture.target_augmentation_index
    if len(target_file_index) != len(target_augmentation_index):
        raise SonusAIError('target_file_index and target_augmentation_index are not the same length')

    if mixture.samples % mixdb.frame_size != 0:
        raise SonusAIError(f'Number of samples in mixture is not a multiple of {mixdb.frame_size}')

    target_audios = list()
    for idx in range(len(mixture.target_file_index)):
        target_augmentation = mixdb.target_augmentations[target_augmentation_index[idx]]

        target_audio = apply_augmentation(audio_in=raw_target_audios[target_file_index[idx]],
                                          augmentation=target_augmentation,
                                          length_common_denominator=mixdb.feature_step_samples)

        target_audio = np.int16(np.round(np.single(target_audio) * mixture.target_snr_gain))
        target_audio = pad_to_samples(audio_in=target_audio, samples=mixture.samples)
        target_audios.append(target_audio)

    raw_noise_audio = raw_noise_audios[mixture.noise_file_index][mixture.noise_augmentation_index]
    noise_audio, _ = get_next_noise(offset_in=mixture.noise_offset,
                                    length=mixture.samples,
                                    audio_in=raw_noise_audio)

    noise_audio = np.int16(np.round(np.single(noise_audio) * mixture.noise_snr_gain))

    return target_audios, noise_audio


def pad_to_samples(audio_in: np.ndarray, samples: int) -> np.ndarray:
    return np.pad(audio_in, (0, samples - len(audio_in)), mode='constant', constant_values=0)


def get_audio_and_truth_t(mixdb: MixtureDatabase,
                          mixture: Mixture,
                          raw_target_audios: List[np.ndarray],
                          raw_noise_audios: List[List[np.ndarray]],
                          compute_truth: bool = True,
                          compute_segsnr: bool = False,
                          frame_based_segsnr: bool = False) \
        -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    from sonusai.mixture import generate_segsnr
    from sonusai.mixture import generate_truth

    target_audios, noise_audio = get_target_noise_audio(mixdb=mixdb,
                                                        mixture=mixture,
                                                        raw_target_audios=raw_target_audios,
                                                        raw_noise_audios=raw_noise_audios)

    truth_t = generate_truth(mixdb=mixdb,
                             mixture=mixture,
                             target_audios=target_audios,
                             noise_audio=noise_audio,
                             compute=compute_truth)

    target_audio = sum(target_audios)

    segsnr = generate_segsnr(mixdb=mixdb,
                             mixture=mixture,
                             target_audio=target_audio,
                             noise_audio=noise_audio,
                             compute=compute_segsnr,
                             frame_based=frame_based_segsnr)

    mixture_audio = target_audio + noise_audio
    return mixture_audio, truth_t, target_audio, noise_audio, segsnr


def get_next_noise(offset_in: int, length: int, audio_in: np.ndarray) -> (np.ndarray, int):
    audio_out = np.take(audio_in, range(offset_in, offset_in + length), mode='wrap')
    offset_out = (offset_in + length) % len(audio_in)
    return audio_out, offset_out


def read_audio(name: str) -> np.ndarray:
    import sox

    from sonusai import SonusAIError
    from sonusai import logger
    from sonusai.mixture import tokenized_expandvars
    from sonusai.mixture import BIT_DEPTH
    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_RATE

    expanded_name, _ = tokenized_expandvars(name)

    try:
        # Read in and convert to desired format
        inp = sox.Transformer()
        inp.set_output_format(rate=SAMPLE_RATE, bits=BIT_DEPTH, channels=CHANNEL_COUNT)
        return inp.build_array(input_filepath=expanded_name,
                               sample_rate_in=int(sox.file_info.sample_rate(expanded_name)))

    except Exception as e:
        if name != expanded_name:
            logger.error(f'Error reading {name} (expanded: {expanded_name}): {e}')
        else:
            raise SonusAIError(f'Error reading {name}: {e}')


@dataclass(frozen=True)
class MixtureData:
    mixture: np.ndarray
    target: List[Union[np.ndarray, None]]
    noise: np.ndarray
    feature: np.ndarray
    truth_f: np.ndarray


def get_mixture_data(mixdb: MixtureDatabase, mixid: int) -> MixtureData:
    """Get mixture data assuming nothing has been loaded into memory already."""

    from sonusai.mixture import apply_augmentation
    from sonusai.mixture import get_feature_and_truth_f
    from sonusai.mixture import get_truth_indices_for_target
    from sonusai.mixture import generate_truth

    mixture = mixdb.mixtures[mixid]

    target_audios = list()
    target_truth_indices = list()
    for idx in range(len(mixture.target_file_index)):
        target_name = mixdb.targets[mixture.target_file_index[idx]].name
        target_augmentation = mixdb.target_augmentations[mixture.target_augmentation_index[idx]]

        target_audio = apply_augmentation(audio_in=read_audio(target_name),
                                          augmentation=target_augmentation,
                                          length_common_denominator=mixdb.feature_step_samples)

        target_audio = np.int16(np.round(np.single(target_audio) * mixture.target_snr_gain))
        target_audio = pad_to_samples(audio_in=target_audio, samples=mixture.samples)
        target_audios.append(target_audio)
        target_truth_indices.append(get_truth_indices_for_target(mixdb.targets[mixture.target_file_index[idx]]))

    raw_noise_audios = build_noise_audios(mixdb=mixdb, show_progress=False)
    raw_noise_audio = raw_noise_audios[mixture.noise_file_index][mixture.noise_augmentation_index]
    noise_audio, _ = get_next_noise(offset_in=mixture.noise_offset,
                                    length=mixture.samples,
                                    audio_in=raw_noise_audio)

    noise_audio = np.int16(np.round(np.single(noise_audio) * mixture.noise_snr_gain))

    truth_t = generate_truth(mixdb=mixdb,
                             mixture=mixture,
                             target_audios=target_audios,
                             noise_audio=noise_audio,
                             compute=True)

    mixture_audio = sum(target_audios) + noise_audio

    # Transform target_audio into a list num_classes long such that each entry is the target data per class
    class_audio = list()
    for n in range(mixdb.num_classes):
        class_audio.append(None)
        for idx in range(len(target_audios)):
            if n + 1 in target_truth_indices[idx]:
                if class_audio[n] is None:
                    class_audio[n] = target_audios[idx]
                else:
                    class_audio[n] += target_audios[idx]

    feature, truth_f = get_feature_and_truth_f(mixdb=mixdb,
                                               mixid=mixid,
                                               audio=mixture_audio,
                                               truth_t=truth_t)

    return MixtureData(mixture=mixture_audio,
                       target=class_audio,
                       noise=noise_audio,
                       feature=feature,
                       truth_f=truth_f)
