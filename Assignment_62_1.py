# Write a Python program to manually perform convolution.

# Input Image (5x5)
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Kernel (3x3)
kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

feature_map = []

for i in range(len(image) - 2):
    row = []
    for j in range(len(image[0]) - 2):

        print(f"\n--- Region at position ({i},{j}) ---")

        total = 0

        for ki in range(3):
            for kj in range(3):
                val = image[i + ki][j + kj]
                weight = kernel[ki][kj]
                mul = val * weight

                print(f"{val}*{weight} = {mul}")
                total += mul

        print("Region Output =", total)
        row.append(total)

    feature_map.append(row)

print("\nFinal Feature Map:")
for r in feature_map:
    print(r)