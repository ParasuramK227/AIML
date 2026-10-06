#Linear regression model using randomly created dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)

X = np.random.rand(50, 1) * 10
y = 2.5 * X + 5 + np.random.randn(50, 1) * 2

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X)

print("Slope (Coefficient):", model.coef_[0][0])
print("Intercept:", model.intercept_[0])

new_X = [[8]]
prediction = model.predict(new_X)

print("Prediction for X = 8:", prediction[0][0])

plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()

plt.show()
