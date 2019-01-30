import meditool.data_types.signal.io as sio
from typing import Tuple
import numpy as np



def read_signal(file_path: str) -> Tuple[int, np.ndarray]:
    """Method for reading EMG signals.
        :param file_path: Path to signal file. Supported file types are: *.wav"
        :type file_path: str
        :return: Tuple. First element is sample rate, second element is numpy.ndarray with signal values.
        :rtype: Tuple[int, numpy.ndarray]
    """

    if file_path.lower().endswith('.wav'):
        return sio.read_wav(file_path)
    else:
        raise ValueError("File extension not supported. Supported extensions are: wav.")

