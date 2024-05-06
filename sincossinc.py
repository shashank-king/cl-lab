import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5 * np.pi, 5 * np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_sinc = np.sinc(x)
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')
y_sinc[x == 0] = 1
plt.plot(x, y_sinc, label='Sinc')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine, Cosine, and Sinc Functions')
plt.legend()
plt.grid(True)
plt.show()
