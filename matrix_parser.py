def read(file):
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
    with open(file, 'r') as f:
        test_cases = int(f.readline())
        toeplitzes = []
        vectors = []
        for _ in range(test_cases):
            size = int(f.readline())
            toeplitzes.append(list(map(int, f.readline().split())))
            f.readline()
            vectors.append(list(map(int, f.readline().split())))
            f.readline()
        return toeplitzes, vectors
