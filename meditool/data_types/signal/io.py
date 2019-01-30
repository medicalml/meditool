import scipy.io.wavfile
import numpy as np
from typing import Tuple


def read_wav(file_path: str) -> Tuple[int, np.ndarray]:
    """Method for reading .wav files.
        :param file_path: Path to .wav file
        :type file_path: str
        :return: Tuple. First element is sampling rate, second element is numpy.ndarray with signal values.
        :rtype: Tuple[int, numpy.ndarray]
    """
    return scipy.io.wavfile.read(file_path)
