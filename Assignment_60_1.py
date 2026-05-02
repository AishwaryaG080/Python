# Write a Python program to simulate a single artificial neuron.

import math

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# Calculated weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias
print("Weighted Sum : ",weighted_sum)

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

output = sigmoid(weighted_sum)

# Display final output
print("Final output : ",output)

if output > 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")