import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt




def turns(fp: int,signal :np.ndarray ,const: float) -> int:
    """Method for counting number of turns in signal.
    :param fp: sampling rate
    :param signal:  numpy.ndarray with signal values
    :param const: parameter that defines multiple of standard deviation. This multiple is a minimum value of signal change which function interprets as a turn.
    :type fp: int
    :type signal: np.ndarray
    type const: float
    :return: Integer. Number of turns in signal bigger than value of standard deviation
    :rtype: int
    """
    dl = signal.size
    dl=dl/fp
    t = np.arange(0,dl,1/fp)

    standard_deviation = np.std(signal)
    standard_deviation = const*standard_deviation
    # print(standard_deviation)
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

    print(standard_deviation)
    # print(number_of_turns)
    plt.plot(t,signal)
    plt.show()
    return number_of_turns
