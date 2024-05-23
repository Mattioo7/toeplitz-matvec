import numpy as np
import sys
import multiplication as mp
import matrix_parser as mpar


def extract_toeplitz_components(toeplitz):
    n = (len(toeplitz) + 1) // 2
    toeplitz_col = toeplitz[:n]
    toeplitz_row = np.concatenate(([toeplitz[0]], toeplitz[n:][::-1]))
    return toeplitz_col, toeplitz_row


if __name__ == '__main__':
    toeplitzes, vectors = mpar.read(sys.argv[1])
    assert len(toeplitzes) == len(vectors)

    all_matching = True
    for i in range(len(toeplitzes)):
        toeplitz = toeplitzes[i]
        vector = np.array(vectors[i])

        toeplitz_col, toeplitz_row = extract_toeplitz_components(toeplitz)

        fast_result_1 = mp.toeplitz_matvec_padded(toeplitz, vector)
        fast_result_2 = mp.toeplitz_vector_mult_custom_fft(toeplitz, vector)
        # fast_result_3 = mp.toeplitz_matvec(toeplitz_col, toeplitz_row, vector)

        print(f"Multiplication result no. {i + 1} is {fast_result_1}")
        print(f"Multiplication result no. {i + 1} is {fast_result_2}")
        # print(f"Multiplication result no. {i + 1} is {fast_result_3}")
