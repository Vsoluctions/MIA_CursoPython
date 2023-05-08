import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5.0,5.0,0.01)
y = np.sin(np.pi*x)

#Graficar
plt.plot(x,y)
plt.title("Ejemplo de grafica")
plt.xlabel("Eje X")
plt.ylabel("Eje X")
plt.show()