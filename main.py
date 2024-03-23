import numpy as np
import sys
import multiplication as mp
import matrix_parser as mpar

if __name__ == '__main__':
    matrices, vectors = mpar.read(sys.argv[1])
    assert len(matrices) == len(vectors)

    all_matching = True
    for i in range(len(matrices)):
        matrix = np.array(matrices[i])
        vector = np.array(vectors[i])
        fast_result = mp.toeplitz_vector_mult_fft(matrix, vector)
        normal_result = mp.normal_mult(matrix, vector)

        if not np.allclose(fast_result, normal_result):
            print("Results are different")
            print("Fast result:", fast_result)
            print("Normal result:", normal_result)
            all_matching = False
    
    if all_matching:
        print("All results match!")
