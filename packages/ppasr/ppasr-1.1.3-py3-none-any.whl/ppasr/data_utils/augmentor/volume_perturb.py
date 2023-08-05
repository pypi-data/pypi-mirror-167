"""Contains the volume perturb augmentation model."""
from ppasr.data_utils.audio import AudioSegment

from ppasr.data_utils.augmentor.base import AugmentorBase


class VolumePerturbAugmentor(AugmentorBase):
    """添加随机音量扰动的增强模型
    
    This is used for multi-loudness training of PCEN. See

    https://arxiv.org/pdf/1607.05666v1.pdf

    for more details.

    :param rng: Random generator object.
    :type rng: random.Random
    :param min_gain_dBFS: Minimal gain in dBFS.
    :type min_gain_dBFS: float
    :param max_gain_dBFS: Maximal gain in dBFS.
    :type max_gain_dBFS: float
    """

    def __init__(self, rng, min_gain_dBFS, max_gain_dBFS):
        self._min_gain_dBFS = min_gain_dBFS
        self._max_gain_dBFS = max_gain_dBFS
        self._rng = rng

    def transform_audio(self, audio_segment: AudioSegment):
        """Change audio loadness.

        Note that this is an in-place transformation.

        :param audio_segment: Audio segment to add effects to.
        :type audio_segment: AudioSegmenet|SpeechSegment
        """
        gain = self._rng.uniform(self._min_gain_dBFS, self._max_gain_dBFS)
        audio_segment.gain_db(gain)
