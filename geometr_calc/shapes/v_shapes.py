from shapes.shape import Shape


class Sphere(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][0]
        )
    


class Cube(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][1]
        )
    


class Paralld(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][2]
        )
    


class Pyram(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][3]
        )
    


class Cilinder(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][4]
        )
    


class Conus(Shape):
    
    
    def __init__(self, **lis):
        super().__init__()
        
        
        self.title = '{0:}'.format(
            Shape.store_fg['объём'][5]
        )