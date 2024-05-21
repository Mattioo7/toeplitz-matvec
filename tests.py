import sys
import matrix_parser as mpar
import multiplication as mp
import time
import numpy as np

def main():
    toeplitzes, vectors = mpar.read(sys.argv[1])
    totalNormalTime, totalFastTime, successCount = 0, 0, 0
    for i in range(len(toeplitzes)):
        toplitz = toeplitzes[i]
        vector = vectors[i]
        normalTime, fastTime = 0, 0
        normalResult, fastResult = None, None
        for _ in range(10):
            start = time.time()
            fastResult = mp.toeplitz_vector_mult_fft(toplitz, vector)
            end = time.time()
            fastTime += end - start

            start = time.time()
            normalResult = mp.normal_mult(mp.matrix_from_toeplitz(toplitz), vector)
            end = time.time()
            normalTime += end - start
        totalNormalTime += normalTime / 10
        totalFastTime += fastTime / 10

        if check_equality(normalResult, fastResult):
            successCount += 1
        else:
            print(f"Results do not match for test case {i + 1}")

    

    print(f"Total time for normal multiplication: {totalNormalTime:.5f}")
    print(f"Total time for fast multiplication: {totalFastTime:.5f}")

    print(f"Success rate: {successCount}/{len(toeplitzes)}")

def check_equality(a, b):
    return np.allclose(a, b)

if __name__ == "__main__":
    main()
