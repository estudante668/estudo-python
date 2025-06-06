import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)
plt.plot(t, y)
plt.title("Gráfico de Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Eixo Y")
plt.show()

