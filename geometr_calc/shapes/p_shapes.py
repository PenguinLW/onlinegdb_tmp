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
        from math import sin, cos, sqrt
        
        x0 = random.randint(1, 50)
        y0 = random.randint(1, 50)
        r = random.randint(1, 10)
        
        xs = [x0 + r * cos(0)]
        ys = [y0 + r * sin(0)]
                
        for i in range(1, 360):
            x = x0 + r * cos(i)
            y = y0 + r * sin(i)
            # if sqrt(x**2 + y**2) == r**2:
            xs.append(x)
            ys.append(y)
        
        xs.append(xs[0])
        ys.append(ys[0])
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
