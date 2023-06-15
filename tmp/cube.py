import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание списка вершин куба
vertices = np.array([(x, y, z)
                for x in [0, 1]
                for y in [0, 1]
                for z in [0, 1]])

# Создание списка граней куба
faces = np.array([(0, 1, 3, 2),
                  (4, 5, 7, 6),
                  (0, 1, 5, 4),
                  (2, 3, 7, 6),
                  (0, 2, 6, 4),
                  (1, 3, 7, 5)])

# Использование созданных списков вершин и граней для построения куба
ax.add_collection3d(
    Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='b')
)

# установить размеры осей и названия
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()