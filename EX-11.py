import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np

# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output data (OR gate)
y = np.array([0, 1, 1, 1])

# Create the neural network
model = Sequential([
    Input(shape=(2,)),
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    X,
    y,
    epochs=1000,
    verbose=0
)

# Evaluate the model
loss, accuracy = model.evaluate(X, y, verbose=0)
print("Accuracy:", accuracy)

# Make a prediction
prediction = model.predict(
    np.array([[1, 0]]),
    verbose=0
)

print("Prediction:", prediction)
