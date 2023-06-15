import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Определение параметров конуса
r = 1
h = 2
resolution = 50

# Генерация координат вершин конуса
theta = np.linspace(0, 2*np.pi, resolution)
z = np.linspace(0, h, resolution)
theta, z = np.meshgrid(theta, z)
x = r * (h-z) / h * np.cos(theta)
y = r * (h-z) / h * np.sin(theta)

# Использование созданных координат для построения поверхности конуса
ax.plot_surface(x, y, z, alpha=0.7)

# установить размеры осей и названия
# ax.set_xlim([0,1])
# ax.set_ylim([0,1])
# ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()