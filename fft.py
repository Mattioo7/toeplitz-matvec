import cmath

import numpy as np



def fft(x):
    """
    A mixed-radix implementation of the 1D Cooley-Tukey FFT,
    that works for any input length.
    """
    N = len(x)
    if N <= 1:
        return x
    elif N % 2 == 0:
        # If N is even, use the standard Cooley-Tukey FFT
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        X = np.concatenate([X_even + factor[:N // 2] * X_odd,
                            X_even + factor[N // 2:] * X_odd])
        return X
    else:
        # If N is odd, use the mixed-radix approach
        X = np.zeros(N, dtype=complex)
        for k in range(N):
            for n in range(N):
                X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
        return X


def ifft(X):
    """
    A recursive implementation of
    the 1D Cooley-Tukey IFFT.
    """
    N = len(X)

    # Take the conjugate of the input
    X_conj = np.conjugate(X)

    # Perform FFT on the conjugated input
    x = fft(X_conj)

    # Take the conjugate of the result and scale by 1/N
    x = np.conjugate(x) / N

    return x
