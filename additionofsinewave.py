import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t = np.arange(0,10,0.3)  # Time range
f1 = 2  # Frequency of first sine wave
f2 = 3  # Frequency of second sine wave
a1 = 1  # Amplitude of first sine wave
a2 = 2  # Amplitude of second sine wave

# Generate sine waves
y1 = a1 * np.sin(2 * np.pi * f1 * t)
y2 = a2 * np.sin(2 * np.pi * f2 * t)

# Add and subtract
y_sum = y1 + y2
y_diff = y1 - y2
plt.plot(t, y_sum, label='Sum')
plt.plot(t, y_diff, label='Difference')
plt.legend()
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Addition and Subtraction of Sine Waves')
plt.show()

