import random
import sys

def generate_toeplitz(size, min, max):
    """
    Generate toeplitz characteristic vector and vector to multiply by
    """
    toeplitz, vector = [], []

    for i in range(2*size - 1):
        toeplitz.append(random.randint(min, max))

    for i in range(size):
        vector.append(random.randint(min, max))
    return toeplitz, vector

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
            toeplitz, vector = generate_toeplitz(size, min, max)
            f.write(" ".join(map(str, toeplitz)))
            f.write("\n\n")
            f.write(" ".join(map(str, vector)))
            f.write("\n\n")
