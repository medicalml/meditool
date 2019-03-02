from typing import Union
import numpy as np 

def arc_length(signal: np.ndarray, sample_rate: Union[int, float]) -> float:
	"""Method for calcualting the arc length of a signal using Euclidian distance.
		:param signal: The signal represented as 1 dimensional numpy array
		:type signal: np.ndarray
		:param sample_rate: Sample rate of a signal used to calculate Euclidean distance between following samples
		:type sample_rate: Union[int, float]
		:return: Float. Calculated arc length  
		:rtype: float
	"""
    values = np.power((signal[1:] - signal[:-1]).astype('float32'), 2)
    distance = np.power(float(1/sample_rate), 2)
    euclidean = np.sqrt(distance  + values)
    total_length = np.sum(euclidean)
    return total_length


