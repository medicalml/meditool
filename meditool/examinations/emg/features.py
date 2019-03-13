import meditool.data_types.signal.features as sfeatures


def root_mean_squares(signal: np.ndarray, window_size: int):
    """Method for computing RMS (root mean squares) of signal.
    :param signal: numpy.ndarray with signal values
    :param window_size: sliding window size. Method computes RMS values in such windows, resulting signal consists of RMS values from consecutive windows.
    :type signal: np.ndarray
    type window_size: int
    :return: Numpy array with RMS values.
    :rtype: np.ndarray
    """
    if type(signal) == np.ndarray and type(window_size) == int:
        sfeatures.root_mean_squares(signal, window_size)
    else:
        raise ValueError("Wrong variable types! Signal should be 1 dimensional numpy array, window_size should be int.")
    
