import numpy as np
import matplotlib.pyplot as plt

def y(t):
    return (1 - (5/2) * t) * np.exp(-3/2 * t)

t = np.linspace(0, 1, 5)

y_values = y(t)

plt.plot(t, y_values, label='y(t) = (1 - 5/2 * t) * exp(-3/2 * t)')
plt.title('Solução da equação diferencial')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()
