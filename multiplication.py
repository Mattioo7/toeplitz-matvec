import numpy as np

def toeplitz_vector_mult_fft(toeplitz, vec):
    """
    Multiply a Toeplitz specification vector by a vector using FFT in O(n log n).

    Parameters:
    - toeplitz: The vector describing Toeplitz matrix.
    - vec: Vector to be multiplied.

    Returns:
    - Result of the multiplication.
    """
    
    n = len(vec)
    m_ext = toeplitz
    v_ext = np.concatenate((vec, np.zeros(n - 1)))

    fft_r = np.fft.fft(m_ext)
    fft_v = np.fft.fft(v_ext)

    fft_result = fft_r * fft_v
    res = np.fft.ifft(fft_result)

    return np.real(res[:n])

def normal_mult(matrix, vec):
    """
    Multiply a matrix by a vector in O(n^2).

    Parameters:
    - matrix: The matrix.
    - vec: Vector to be multiplied.

    Returns:
    - Result of the multiplication.
    """

    return matrix @ vec
