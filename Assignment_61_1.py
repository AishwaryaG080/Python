# Create a neural network model to predict whether a customer will leave a service.

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create Dataset
X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

Y = np.array([0,0,1,1,0,0,1,1,0,1])

# Apply StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, Y, test_size=0.2, random_state=42
)

model = Sequential()

model.add(Dense(8, activation='relu', input_dim=5))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(  
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=50, verbose=0)

# Evaluate Accuracy
y_pred = model.predict(X_test) > 0.5
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy: ",accuracy)

# Test Input
new_customer = np.array([[46, 1450, 5, 6, 9]])

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

print("\nPrediction Probability: ",prediction[0][0])

if prediction[0][0] > 0.5:
    print("Customer may leave")
else:
    print("Customer will stay")