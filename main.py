import numpy as np


def toeplitz_vector_mult_fft(col, row, vec):
    """
    Multiply a Toeplitz matrix by a vector using FFT in O(n log n).

    Parameters:
    - col: First column of the Toeplitz matrix.
    - row: First row of the Toeplitz matrix.
    - vec: Vector to be multiplied.

    Returns:
    - Result of the multiplication.
    """

    n = len(vec)
    m_ext = np.concatenate((col, row[:0:-1]))
    v_ext = np.concatenate((vec, np.zeros(n - 1)))

    fft_r = np.fft.fft(m_ext)
    fft_v = np.fft.fft(v_ext)

    fft_result = fft_r * fft_v
    res = np.fft.ifft(fft_result)

    return np.real(res[:n])


if __name__ == '__main__':
    row = np.array([1, 2, 3])  # First row of the Toeplitz matrix
    col = np.array([1, 4, 5])  # First column of the Toeplitz matrix
    vec = np.array([1, 2, 3])  # Vector to multiply
    result = toeplitz_vector_mult_fft(col, row, vec)
    print("Result:", result)

    expected_result = np.array([14, 12, 16])
    if np.allclose(result, expected_result):
        print("The result matches the expected value.")
    else:
        print("The result does not match the expected value.")
