
"""
Read a file and return a matrix and a vector list
File needs to be in the following format:
- The first line contains the number of test cases.
- The next line contains the number of rows and columns of the matrix.
- The next lines contain the matrix elements separated by spaces.
- Then there is an empty line.
- The next line contains the vector elements separated by spaces.
- Then there is an empty line
- The process repeats for the number of test cases.
- The file ends with an empty line.
"""
def read(file):
    with open(file, 'r') as f:
        test_cases = int(f.readline())
        matrices = []
        vectors = []
        for _ in range(test_cases):
            rows = int(f.readline())
            matrix = []
            for _ in range(rows):
                matrix.append(list(map(int, f.readline().split())))
            matrices.append(matrix)
            f.readline()
            vectors.append(list(map(int, f.readline().split())))
            f.readline()
        return matrices, vectors
