import random

sizes = [5, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 2000, 5000, 7500, 10000]
count = 10
min = -100
max = 100

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

for size in sizes:
    seed = random.randint(0, 1000000)
    filename = f"visualization/{count}C_{size}S_range_{min}_{max}_seed_{seed}.txt"
    print(f"Generating file {filename}")

    with open(filename, 'w') as f:
        f.write(f"{count}\n")
        for _ in range(count):
            f.write(f"{size}\n")
            toeplitz, vector = generate_toeplitz(size, min, max)
            f.write(" ".join(map(str, toeplitz)))
            f.write("\n\n")
            f.write(" ".join(map(str, vector)))
            f.write("\n\n")
