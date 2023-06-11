from shapes.shape import Shape


class Sphere(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][0]
        )

    @staticmethod
    def random_sphere():
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys


class Cube(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][1]
        )

    @staticmethod
    def random_cube():
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys


class Paralld(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][2]
        )

    @staticmethod
    def random_paralld():
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys


class Pyram(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][3]
        )

    @staticmethod
    def random_pyram():
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys


class Cilinder(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][4]
        )

    @staticmethod
    def random_cilinder():
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys


class Conus(Shape):
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][5]
        )

    @staticmethod
    def random_conus():

        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys