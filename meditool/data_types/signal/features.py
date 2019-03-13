import numpy as np


def turns(signal :np.ndarray ,minimal_signal_change: float) -> int:
    """Method for counting number of turns in signal.
    :param signal:  numpy.ndarray with signal values
    :param minimal_signal_change: parameter that defines multiple of standard deviation. This multiple is a minimum value of signal change which function interprets as a turn.
    :type signal: np.ndarray
    type minimal_signal_change: float
    :return: Integer. Number of turns in signal bigger than value of standard deviation multipled by minimal_signal_change parameter
    :rtype: int
    """

    standard_deviation = np.std(signal)
    standard_deviation = minimal_signal_change*standard_deviation

    sign1=signal[1]-signal[0]
    sign2=signal[2]-signal[1]
    point0 = signal[0]
    point1= signal[1]

    number_of_turns=0
    for i in range(signal.size-2):
        sign1=signal[i+1]-signal[i]
        sign2=signal[i+2]-signal[i+1]
        if((sign1>0 and sign2<0) or (sign1<0 and sign2>0)):
            point1 = signal[i+1]

            if(abs(point0-point1)>abs(standard_deviation)):
                number_of_turns+=1
                point0=point1


    return number_of_turns
