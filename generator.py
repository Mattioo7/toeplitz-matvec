import random
import sys

def generate_toeplitz(size, min, max):
    """
    Generates a Toeplitz matrix and a vector to multiply it with.
    """
    # Initalize the matrix size
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    vector = []
    # Fill the matrix
    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0:
                matrix[i][j] = random.randint(min, max)
            else:
                matrix[i][j] = matrix[i-1][j-1]
    
    for i in range(size):
        vector.append(random.randint(min, max))
    return matrix, vector

if __name__ == "__main__":
    count = int(sys.argv[1])
    size = int(sys.argv[2])
    min = int(sys.argv[3])
    max = int(sys.argv[4])
    filename = sys.argv[5]
    seed = int(sys.argv[6])

    random.seed(seed)
    
    with open(filename, 'w') as f:
        f.write(f"{count}\n")
        for _ in range(count):
            f.write(f"{size}\n")
            matrix, vector = generate_toeplitz(size, min, max)
            for row in matrix:
                f.write(" ".join(map(str, row)))
                f.write("\n")
            f.write("\n")
            f.write(" ".join(map(str, vector)))
            f.write("\n\n")
