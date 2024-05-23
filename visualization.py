import os
import sys
import time
import matplotlib.pyplot as plt
import matrix_parser as mpar
import multiplication as mp

def process_files(file_list):
    timings_fast = []
    timings_normal = []
    for file in file_list:
        print(f'Processing file {file}')
        toeplitzes, vectors = mpar.read(file)
        totalNormalTime, totalFastTime = 0, 0
        for i in range(len(toeplitzes)):
            print(f'Processing test case {i + 1}')
            toplitz = toeplitzes[i]
            vector = vectors[i]
            start = time.time()
            mp.toeplitz_vector_mult_fft(toplitz, vector)
            end = time.time()
            totalFastTime += end - start

            start = time.time()
            mp.normal_mult(mp.matrix_from_toeplitz(toplitz), vector)
            end = time.time()
            totalNormalTime += end - start
        timings_fast.append((len(vectors[0]), totalFastTime / len(vectors)))
        timings_normal.append((len(vectors[0]), totalNormalTime / len(vectors)))

    return timings_fast, timings_normal

def plot_timings(timings_fast, timings_normal):
    # timings are list of tuples. First item is the size of the vector, second item is the average time

    # sort the timings by the size of the vector
    timings_fast.sort(key=lambda x: x[0])
    timings_normal.sort(key=lambda x: x[0])

    x_fast = [x[0] for x in timings_fast]
    y_fast = [y[1] for y in timings_fast]
    x_normal = [x[0] for x in timings_normal]
    y_normal = [y[1] for y in timings_normal]

    # plot log on y axis
    plt.plot(x_fast, y_fast, label='FFT')
    plt.plot(x_normal, y_normal, label='Normal')
    plt.yscale('log')
    plt.xlabel('Vector size')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    files = os.listdir('visualization')
    files = [os.path.join('visualization', file) for file in files]
    timings_fast, timings_normal = process_files(files)
    plot_timings(timings_fast, timings_normal)
