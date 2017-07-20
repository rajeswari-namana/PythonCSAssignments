#importing modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#dummy data
n_samples = 200
X = np.random.normal(size=n_samples)
y = (X > 0).astype(np.float)
X[X > 0] *= 4
X += .3 * np.random.normal(size=n_samples)
X = X[:, np.newaxis]

# run the classifier
clf = linear_model.LogisticRegression(C=1e5)
clf.fit(X, y)

# plotting the graph
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(X.ravel(), y, color='g', zorder=20)
X_test = np.linspace(-10, 12, 100)

#Logistic function
def logisticModel(x):
    return 1 / (1 + np.exp(-x))

#function call
loss =logisticModel(X_test * clf.coef_ + clf.intercept_).ravel()

#plotting the output
plt.plot(X_test, loss, color='b', linewidth=3)
plt.axhline(0.5, color='r')
plt.title("Sugar levels - diabetic or not")
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
