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

class Rect(Square):
    
    def __init__(self, **lis):
        
        self.title = '{0:}'.format(
            Shape.store_fg['плоскость'][2]
        )
        
        for key, value in lis.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative") 
            setattr(self, key, value)
    
    
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