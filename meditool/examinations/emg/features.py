import meditool.data_types.signal.features as sfeatures
from typing import Union
import numpy as np

def arc_length(signal: np.ndarray, sample_rate: Union[int, float]) -> float:
    """Method for calcualting the arc length of an EMG signal using Euclidian distance.
	:param signal: The signal represented as 1 dimensional numpy array
	:type signal: np.ndarray
	:param sample_rate: Sample rate of a signal used to calculate Euclidean distance between following samples
	:type sample_rate: Union[int, float]
	:return: Float. Calculated arc length  
	:rtype: float
    """
    if type(signal) == np.ndarray) and type(sample_rate) == (int or float):
	return sfeatures.arc_length(signal, sample_rate)
    else:
        raise ValueError("Wrong variable types! Signal should be 1 dimensional numpy array, sample_rare should be int or float.")


def envelope(signal: np.ndarray) -> np.ndarray:
    """Method for calculating the evelope of an EMG signal.
	:param signal: The signal represented as 1 dimensional numpy array
	:type signal: np.ndarray
	:return: Numpy array with envelope values
	:rtype: np.ndarray
    """
    if type(signal) == np.ndarray:
	return sfeatures.envelope(signal)
    else:
	raise ValueError("Wrong variable type! Signal should be 1 dimensional numpy array.")
    
