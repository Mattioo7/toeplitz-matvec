import numpy as np


def fft(x):
    """
    A recursive implementation of
    the 1D Cooley-Tukey FFT, the
    input should have a length of
    power of 2.
    """
    N = len(x)

    if N == 1:
        return x
    else:
        if N % 2 > 0:
            x = np.append(x, np.zeros(2**int(np.ceil(np.log2(N))) - N))
            N = len(x)

        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)

        X = np.concatenate(
            [X_even + factor[:int(N / 2)] * X_odd,
             X_even + factor[int(N / 2):] * X_odd])
        return X


def ifft(X):
    """
    A recursive implementation of
    the 1D Cooley-Tukey IFFT, the
    input should have a length of
    power of 2.
    """
    N = len(X)

    # Take the conjugate of the input
    X_conj = np.conjugate(X)

    # Perform FFT on the conjugated input
    x = fft(X_conj)

    # Take the conjugate of the result and scale by 1/N
    x = np.conjugate(x) / N

    return x
