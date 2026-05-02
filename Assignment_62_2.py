# Write a Python program to demonstrate ReLU and Max Pooling.

import numpy as np

# 1. Input Feature Map
feature_map = np.array([
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
])

print("Original Feature Map:")
print(feature_map)

# 2. Apply ReLU
relu_output = np.maximum(0, feature_map)

print("\nAfter ReLU:")
print(relu_output)

# 3. Apply 2x2 Max Pooling
pool_size = 2
stride = 1

h, w = relu_output.shape
pooled = []

for i in range(0, h - pool_size + 1, stride):
    row = []
    for j in range(0, w - pool_size + 1, stride):
        region = relu_output[i:i+pool_size, j:j+pool_size]

        print(f"\nRegion ({i},{j}):")
        print(region)

        max_val = np.max(region)
        print("Max Value:", max_val)

        row.append(max_val)
    pooled.append(row)

pooled_output = np.array(pooled)

print("\nFinal Max Pooled Output:")
print(pooled_output)