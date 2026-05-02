# Create a neural network model to predict loan approval.


import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = np.array([
    [25000, 650, 200000, 5000, 0],
    [30000, 700, 300000, 4000, 1],
    [45000, 750, 150000, 10000, 1],
    [50000, 800, 100000, 12000, 0],
    [28000, 680, 250000, 5000, 1],
    [35000, 720, 350000, 3000, 1],
    [48000, 770, 120000, 15000, 0],
    [52000, 820, 90000, 20000, 1],
    [27000, 660, 280000, 4000, 0],
    [42000, 740, 180000, 9000, 1]
])

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = Sequential([
    Dense(10, activation='relu', input_dim=5),
    Dense(6, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=50, verbose=0)

y_pred = model.predict(X_test) > 0.5
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Test Input
new_applicant = np.array([[55000, 720, 400000, 10000, 1]])

new_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_scaled)

print("\nApproval Probability:", prediction[0][0])

if prediction[0][0] > 0.5:
    print("Loan Approved")
else:
    print("Loan Rejected")