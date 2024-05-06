import numpy as np
import matplotlib.pyplot as plt

def f(x):  # Define the function to differentiate
  return x**2 + 3*x + 1

def central_difference(f, x, h):

  return (f(x + h) - f(x - h)) / (2 * h)

# Define the range of x-values
x = np.linspace(-2, 4, 100)

# Calculate numerical derivatives using central difference
dy_dx = np.array([central_difference(f, xi, 0.01) for xi in x])

# Plot the original function and its numerical derivative
plt.plot(x, f(x), label='Original function')
plt.plot(x, dy_dx, label='Numerical derivative (central difference)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Plot of Original Function and Numerical Derivative')
plt.show()

