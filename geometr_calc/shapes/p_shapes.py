from shapes.shape import Shape


class Circle(Shape):
    
    def __init__(self, **lis):
        super().__init__()
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][0]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)
    
    @staticmethod
    def random_circle():
        import random
        from math import sin, cos

        x0 = random.randint(1, 100)
        y0 = random.randint(1, 100)
        r = random.randint(1, 50)
        
        xs = []
        ys = []

        for i in range(0, 360*45, 25):
            x = x0 + r * cos(i)
            y = y0 + r * sin(i)
            xs.append(x)
            ys.append(y)

        return xs, ys

class Square(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][1]
        )
        
#        self.a, self.b = input('a, b = ? ?: ').split()
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)
    
    def count_perimeter(self):
        p = float(self.a)*2 + float(self.b)*2
        return p
    def count_square(self):
        s = float(self.a) * float(self.b)
        return s
    
    @staticmethod
    def random_square():
        
        xs = [2, 2, 3, 3]
        ys = [3, 6, 6, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys

class Rect(Square):
    
    def __init__(self, **lis):
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][2]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)

    @staticmethod
    def random_rect():

        xs = [2, 2, 3, 3]
        ys = [3, 7, 7, 3]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys
    
    
class Triang(Shape):
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][3]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)

    @staticmethod
    def random_triang():

        xs = [2, 2, 3]
        ys = [3, 6, 6]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys
    
    
class Trapec(Shape):
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][4]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)

    @staticmethod
    def random_trapec():

        xs = [2, 4, 5, 6]
        ys = [2, 6, 6, 2]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys
    
    
class Rhombe(Shape):
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][5]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)

    @staticmethod
    def random_rhombe():

        xs = [2, 4, 6, 4]
        ys = [3, 4, 3, 2]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys