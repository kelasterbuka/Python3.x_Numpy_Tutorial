import numpy as np
import matplotlib.pyplot as plt

# persamaan garis
# y = 2x + 3

x = np.arange(0,11,1)
y = 2*x + 3
print(x)
print(y)

plt.figure(1)
plt.plot(x,y)

# lingkaran

jari2 = 5

sudut = np.linspace(0,2*np.pi,100)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)

plt.figure(2)
plt.plot(x2,y2)
plt.show()
