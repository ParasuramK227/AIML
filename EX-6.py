import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Create a random dataset
np.random.seed(42)

X = np.random.rand(50, 1) * 10
y = 2.5 * X + 5 + np.random.randn(50, 1) * 2

# 2. Create the Linear Regression model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)

# 4. Predict values
y_pred = model.predict(X)

# 5. Display model parameters
print("Slope (Coefficient):", model.coef_[0][0])
print("Intercept:", model.intercept_[0])

# 6. Predict for a new value
new_X = [[8]]
prediction = model.predict(new_X)

print("Prediction for X = 8:", prediction[0][0])

# 7. Visualize the results
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()

plt.show()
