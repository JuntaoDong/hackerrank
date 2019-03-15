# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn import linear_model

m, n = map(int, input().strip().split())
x_train = np.empty((0,m))
x_test = np.empty((0,m))
y_train = np.array([])
for i in range(n):
    data = list(map(float, input().strip().split()))
    x_train = np.vstack([x_train, data[:-1]])
    y_train = np.append(y_train, data[-1])
test = int(input())
for j in range(test):
    data = list(map(float, input().strip().split()))
    x_test = np.vstack([x_test, data])

model = linear_model.LinearRegression()
result = model.fit(x_train, y_train)
y_pred = result.predict(x_test)
for i in range(test):
    print(round(y_pred[i], 2))