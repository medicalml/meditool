import numpy as np
from scipy.signal import hilbert

def envelope(signal: np.ndarray) -> np.ndarray:
	"""Method for calculating the evelope of a signal.
		:param signal: The signal represented as 1 dimensional numpy array
		:type signal: np.ndarray
		:return: Numpy array consisting envelope values
		:rtype: np.ndarray
	"""
    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)
    return amplitude_envelope
