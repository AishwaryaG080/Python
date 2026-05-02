# Write a Python program to show flattening.

# 1. Input Matrix (2D)
matrix = [
    [6, 4],
    [8, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 2. Flatten (2D → 1D)
flatten_output = []
for row in matrix:
    for val in row:
        flatten_output.append(val)

print("\nFlatten Output:", flatten_output)

# 3. Fully Connected Layer
weights = [0.2, 0.4, 0.6, 0.8]
bias = 1

# 4. Calculate final output
output = 0
print("\nCalculation Steps:")

for i in range(len(flatten_output)):
    mul = flatten_output[i] * weights[i]
    print(f"{flatten_output[i]} * {weights[i]} = {mul}")
    output += mul

output += bias
print("Add Bias:", bias)

print("\nFinal Output:", output)