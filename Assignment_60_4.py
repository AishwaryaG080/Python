# Write a Python program to show how weights are updated in ANN.

x = 2
w = 0.5
bias = 0.1
target = 1
learning_rate = 0.1

# Calculate Prediction
y_pred = (x * w) + bias

# Calculate Error
error = target - y_pred

# Update weight using Gradient Descent
updated_weight = w + learning_rate * error * x

print("Input: ",x)
print("Target: ",target)

print("\n----- Old Weight -----")
print("Weight: ",w)
print("Prediction: ",y_pred)
print("Error: ",error)

print("\n----- Updated Weight -----")
print("Updated Weight: ",updated_weight)