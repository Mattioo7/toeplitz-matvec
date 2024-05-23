import numpy as np
import fft


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


def toeplitz_vector_mult_fft_custom(toeplitz, vec):
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

    fft_r = fft.fft(m_ext)
    fft_v = fft.fft(v_ext)

    fft_result = fft_r * fft_v
    res = fft.ifft(fft_result)

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


def matrix_from_toeplitz(toeplitz):
    """
    Generate a Toeplitz matrix from a Toeplitz vector.

    Parameters:
    - toeplitz: The vector describing Toeplitz matrix.

    Returns:
    - The Toeplitz matrix.
    """
    
    size = (int)((len(toeplitz) + 1) / 2)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        matrix[i][0] = toeplitz[i]

    rev = list(reversed(toeplitz))
    for i in range(1, size):
        matrix[0][i] = rev[i - 1]
    for i in range(1, size):
        for j in range(1, size):
            matrix[i][j] = matrix[i-1][j-1]

    return np.array(matrix)
