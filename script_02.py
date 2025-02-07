# Importar el módulo de Python para graficar
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('Lado de x')
plt.ylabel('Lado de y')
plt.title('Gráfica de la función')
plt.show()