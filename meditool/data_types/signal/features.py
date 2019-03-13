import numpy as np


def root_mean_squares(signal: np.ndarray, window_size: int):
    """Method for computing RMS (root mean squares) of signal.
    :param signal: numpy.ndarray with signal values
    :param window_size: sliding window size. Method computes RMS values in such windows, resulting signal consists of RMS values from consecutive windows.
    :type signal: np.ndarray
    type window_size: int
    :return: Numpy array with RMS values.
    :rtype: np.ndarray
    """
    
    half_size = int(window_size/2)
    lower_bounds = [max(0, i - half_size) for i in range(len(signal))]
    upper_bounds = [min(len(signal) - 1, i + half_size) for i in range(len(signal))]
    def _rms(window):
        return np.sqrt(np.mean(np.square(window)))
    signal_rms = [_rms(signal[low:upp]) for low, upp in zip(lower_bounds, upper_bounds)]
    return np.asarray(signal_rms)
