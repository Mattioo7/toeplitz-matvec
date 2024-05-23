import sys
import matrix_parser as mpar
import multiplication as mp
import time
import numpy as np


def extract_toeplitz_components(toeplitz):
    n = (len(toeplitz) + 1) // 2
    toeplitz_col = toeplitz[:n]
    toeplitz_row = np.concatenate(([toeplitz[0]], toeplitz[n:][::-1]))
    return toeplitz_col, toeplitz_row


def pad_toeplitz(toeplitz_col, toeplitz_row, x):
    n = len(toeplitz_col)
    m = len(x)

    # Construct the circulant matrix's first column
    c = np.zeros(2 * n)
    c[:n] = toeplitz_col
    c[n + 1:] = toeplitz_row[::-1][:-1]

    # Construct the vector for FFT
    x_padded = np.zeros(2 * n)
    x_padded[:m] = x

    return c, x_padded


def main():
    toeplitzes, vectors = mpar.read(sys.argv[1])
    totalNormalTime, totalFastTime_numpy, totalFastTime_custom, successCount = 0, 0, 0, 0
    for i in range(len(toeplitzes)):
        toplitz = toeplitzes[i]
        vector = vectors[i]
        normalTime, fastTime_numpy, fastTime_custom = 0, 0, 0
        normalResult, fastResult_numpy, fastResult_custom = None, None, None

        for _ in range(10):
            toeplitz_col, toeplitz_row = extract_toeplitz_components(toplitz)
            c, x_padded = pad_toeplitz(toeplitz_col, toeplitz_row, vector)

            # fast multiplication by custom fft
            start = time.time()
            fastResult_custom = mp.toeplitz_matvec(c, x_padded)
            end = time.time()
            fastResult_custom = fastResult_custom[:len(toeplitz_col)]
            fastTime_custom += end - start

            # fast multiplication by numpy fft
            start = time.time()
            fastResult_numpy = mp.toeplitz_vector_mult_numpy_fft(toplitz, vector)
            end = time.time()
            fastTime_numpy += end - start

            # normal multiplication
            start = time.time()
            normalResult = mp.normal_mult(mp.matrix_from_toeplitz(toplitz), vector)
            end = time.time()
            normalTime += end - start

        totalNormalTime += normalTime / 10
        totalFastTime_numpy += fastTime_numpy / 10
        totalFastTime_custom += fastTime_custom / 10

        if check_equality(normalResult, fastResult_numpy) and check_equality(normalResult, fastResult_custom):
            successCount += 1
        else:
            print(f"Results do not match for test case {i + 1}")

    

    print(f"Total time for      normal multiplication: {totalNormalTime:.5f}")
    print(f"Total time for  numpy fast multiplication: {totalFastTime_numpy:.5f}")
    print(f"Total time for custom fast multiplication: {totalFastTime_custom:.5f}")

    print(f"Success rate: {successCount}/{len(toeplitzes)}")

def check_equality(a, b):
    return np.allclose(a, b)

if __name__ == "__main__":
    main()
