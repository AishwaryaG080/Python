# Write a Python program to calculate loss manually.

import math

y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.2, 0.8, 0.7]

# Mean Squared Error
def MSE(y_true, y_pred):
    n = len(y_true)
    mse = 0
    for i in range(n):
        mse = mse + (y_true[i] - y_pred[i]) ** 2
    return mse / n

# Binary Cross Entropy
def BCE(y_true, y_pred):
    n = len(y_true)
    bce = 0
    for i in range(n):
        # Avoid log(0) by adding small epsilon
        epsilon = 1e-10
        x = min(max(y_pred[i], epsilon), 1 - epsilon)
        bce = bce + y_true[i] * math.log(x) + (1 - y_true[i]) * math.log(1 - x)

    return -bce / n

# Calculate Losses
mse_loss = MSE(y_true, y_pred)
bce_loss = BCE(y_true, y_pred)

print("Mean Squared Error : ",mse_loss)
print("Binary Cross Entropy : ",bce_loss)