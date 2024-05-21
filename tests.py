import sys
import matrix_parser as mpar
import multiplication as mp
import time

def main():
    toeplitzes, vectors = mpar.read(sys.argv[1])
    totalNormalTime, totalFastTime = 0, 0
    for i in range(len(toeplitzes)):
        toplitz = toeplitzes[i]
        vector = vectors[i]
        normalTime, fastTime = 0, 0
        for _ in range(10):
            # Time multiplations
            start = time.time()
            mp.toeplitz_vector_mult_fft(toplitz, vector)
            end = time.time()
            fastTime += end - start

            start = time.time()
            mp.normal_mult(mp.matrix_from_toeplitz(toplitz), vector)
            end = time.time()
            normalTime += end - start
        totalNormalTime += normalTime / 10
        totalFastTime += fastTime / 10
    

    print(f"Total time for normal multiplication: {totalNormalTime:.5f}")
    print(f"Total time for fast multiplication: {totalFastTime:.5f}")

if __name__ == "__main__":
    main()
