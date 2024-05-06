import numpy as np
from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
l = len(x)
y = []
for i in range(0, l - 1):
    diff = x[i + 1] - x[i]
    y.append(diff)

plt.plot(x, label='Original Data')
plt.plot(y, label='Differences')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.title('Plot of Original Data and Differences')
plt.show()

