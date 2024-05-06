import numpy as np
import matplotlib.pyplot as plt

# Generate x-values
x_values = np.arange(0, 2*np.pi, 0.01)  # Generating x-values from 0 to 2*pi with a step of 0.01

# Calculate y-values (sine of x)
y_values = np.sin(x_values)

# Plot the sine wave
plt.plot(x_values, y_values)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

