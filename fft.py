import cmath

import numpy as np


def fft_power_of_two(x):
    """
    A recursive implementation of the 1D Cooley-Tukey FFT.
    If the length of the input is not a power of 2, it zero-pads the input.
    Returns the FFT result with the same length as the original input.
    """
    original_length = len(x)

    # Find the next power of two
    if not (original_length & (original_length - 1) == 0 and original_length != 0):
        next_power_of_two = 1 << (original_length - 1).bit_length()
        x = np.concatenate((x, np.zeros(next_power_of_two - original_length)))

    def fft_recursive(x):
        N = len(x)
        if N <= 1:
            return x
        else:
            X_even = fft_recursive(x[::2])
            X_odd = fft_recursive(x[1::2])
            factor = np.exp(-2j * np.pi * np.arange(N) / N)

            X = np.concatenate(
                [X_even + factor[:int(N / 2)] * X_odd,
                 X_even + factor[int(N / 2):] * X_odd])
            return X

    # Compute the FFT
    X_full = fft_recursive(x)

    # Return only the relevant portion (first original_length elements)
    return X_full[:original_length]


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
        # If N is odd, attempt to find a mixed-radix approach
        # Here, we break down N into factors
        factors = prime_factors(N)
        if len(factors) == 1:  # N is prime
            X = np.zeros(N, dtype=complex)
            for k in range(N):
                for n in range(N):
                    X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
            return X
        else:
            # Use the first factor to split the sequence
            factor = factors[0]
            new_length = N // factor
            X = np.zeros(N, dtype=complex)
            for k in range(N):
                for j in range(factor):
                    sub_fft = fft(x[j::factor])
                    factor_exp = np.exp(-2j * np.pi * j * k / N)
                    X[k] += factor_exp * sub_fft[k % new_length]
            return X


def prime_factors(n):
    """Return the prime factors of the given number n."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


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
