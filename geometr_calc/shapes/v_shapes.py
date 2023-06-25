from shapes.shape import Shape

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Sphere(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][0]
        )

    @staticmethod
    def random_sphere(fig, ax):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        x = 2 * np.outer(np.cos(u), np.sin(v))
        y = 2 * np.outer(np.sin(u), np.sin(v))
        z = 2 * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z)
        return fig


class Cube(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][1]
        )

    @staticmethod
    def random_cube(fig, ax):
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
        return fig


class Paralld(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][2]
        )

    @staticmethod
    def random_paralld(fig, ax):
        # Создание списка вершин параллелепипеда
        vertices = np.array([(0, 0, 0),
                             (1, 0, 0),
                             (1, 1, 0),
                             (0, 1, 0),
                             (0, 0, 1),
                             (1, 0, 1),
                             (1, 1, 1),
                             (0, 1, 1)])

        # Создание списка граней параллелепипеда
        faces = np.array([(0, 1, 2, 3),
                          (0, 1, 5, 4),
                          (1, 2, 6, 5),
                          (2, 3, 7, 6),
                          (3, 0, 4, 7),
                          (4, 5, 6, 7)])

        # Использование созданных списков вершин и граней для построения параллелепипеда
        ax.add_collection3d(
            Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='b')
        )
        return fig


class Pyramd(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][3]
        )

    @staticmethod
    def random_pyramd(fig, ax):
        # Координаты вершин пирамиды
        vertices = np.array([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 1)])

        # Номера вершин для построения каждой грани
        faces = np.array([(0, 1, 2), (0, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)])

        # Использование созданных списков вершин и граней для построения пирамиды
        ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='b'))
        return fig


class Cilind(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][4]
        )

    @staticmethod
    def random_cilind(fig, ax):
        # Определение параметров цилиндра
        r = 1
        h = 2
        resolution = 50

        # Генерация координат вершин цилиндра
        theta = np.linspace(0, 2 * np.pi, resolution)
        z = np.linspace(0, h, resolution)
        theta, z = np.meshgrid(theta, z)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        # Использование созданных координат для построения поверхности цилиндра
        ax.plot_surface(x, y, z, alpha=0.7)
        return fig


class Conus(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][5]
        )

    @staticmethod
    def random_conus(fig, ax):
        # Определение параметров конуса
        r = 1
        h = 2
        resolution = 50

        # Генерация координат вершин конуса
        theta = np.linspace(0, 2 * np.pi, resolution)
        z = np.linspace(0, h, resolution)
        theta, z = np.meshgrid(theta, z)
        x = r * (h - z) / h * np.cos(theta)
        y = r * (h - z) / h * np.sin(theta)

        # Использование созданных координат для построения поверхности конуса
        ax.plot_surface(x, y, z, alpha=0.7)
        return fig