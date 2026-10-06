#Feed Forward Network using Tensorflow/Keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1])

model = Sequential([
    Input(shape=(2,)),
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X,
    y,
    epochs=1000,
    verbose=0
)

loss, accuracy = model.evaluate(X, y, verbose=0)
print("Accuracy:", accuracy)

prediction = model.predict(
    np.array([[1, 0]]),
    verbose=0
)

print("Prediction:", prediction)
