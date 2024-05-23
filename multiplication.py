import numpy as np

import fft


def toeplitz_vector_mult_numpy_fft(toeplitz, vec):
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


def toeplitz_vector_mult_custom_fft(toeplitz, vec):
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


def toeplitz_matvec(c, x_padded):
    """
    Perform matrix-vector multiplication with a Toeplitz matrix using FFT.

    Parameters:
    toeplitz_col (ndarray): The first column of the Toeplitz matrix.
    toeplitz_row (ndarray): The first row of the Toeplitz matrix.
    x (ndarray): The vector to be multiplied.

    Returns:
    ndarray: The result of the matrix-vector multiplication.
    """

    # Perform the FFT-based multiplication using your FFT implementation
    fft_c = fft.fft(c)
    fft_x = fft.fft(x_padded)
    fft_result = fft_c * fft_x
    result = fft.ifft(fft_result)

    # Extract the relevant part of the result
    return result.real


def is_power_of_two(n):
    """Check if a number is a power of two."""
    return (n & (n - 1) == 0) and n != 0


def next_power_of_two(n):
    """Find the next power of two greater than or equal to n."""
    return 1 << (n - 1).bit_length()


def toeplitz_matvec_padded(toeplitz, vec):
    """
    Perform matrix-vector multiplication with a Toeplitz matrix using FFT.

    Parameters:
    toeplitz_col (ndarray): The first column of the Toeplitz matrix.
    toeplitz_row (ndarray): The first row of the Toeplitz matrix.
    x (ndarray): The vector to be multiplied.

    Returns:
    ndarray: The result of the matrix-vector multiplication.
    """

    n = len(vec)

    # Check if the length of toeplitz is a power of 2
    if not is_power_of_two(len(toeplitz)):
        # Find the next power of two
        new_length = next_power_of_two(len(toeplitz))

        # Pad toeplitz and vec with zeros
        toeplitz = np.concatenate((toeplitz, np.zeros(new_length - len(toeplitz))))
        vec = np.concatenate((vec, np.zeros(new_length - len(vec))))
    else:
        # Pad vec with zeros
        vec = np.concatenate((vec, np.zeros(n - 1)))

    # Perform the FFT-based multiplication using your FFT implementation
    fft_c = fft.fft_power_of_two(toeplitz)
    fft_x = fft.fft_power_of_two(vec)
    fft_result = fft_c * fft_x
    result = np.fft.ifft(fft_result)

    # Extract the relevant part of the result
    return result.real


def normal_mult(matrix, vec):
    """
    Multiply a matrix by a vector in O(n^2).

    Parameters:
    - matrix: The matrix.
    - vec: Vector to be multiplied.

    Returns:
    - Result of the multiplication.
    """
    result = [0] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(vec)):
            result[i] += matrix[i][j] * vec[j]

    return result

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
