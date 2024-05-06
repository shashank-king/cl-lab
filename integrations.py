import numpy as np
import matplotlib.pyplot as plt

def f(x): 
  return x**2 + 3*x + 1

def trapezoidal_rule(f, a, b, n):
  h = (b - a) / n
  x = np.linspace(a, b, n + 1)
  y = f(x)
  return h * (0.5 * y[0] + sum(y[1:-1]) + 0.5 * y[-1])
a = 0
b = 4
n = 100
integral = trapezoidal_rule(f, a, b, n)
x_plot = np.linspace(a, b, 1000)
plt.plot(x_plot, f(x_plot), label='Original function')
plt.axhline(y=integral, color='r', linestyle='--', label='Numerical integral')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Plot of Original Function and Numerical Integral')
plt.show()

