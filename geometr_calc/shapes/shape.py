
class Shape:
    store_fg = {
        'плоскость': ('круг', 'квадрат', 'прамоугольник', 'треугольник', 'трапеция', 'ромб'),
        'объём': ('сфера', 'куб', 'параллелепипед', 'пирамида', 'цилиндр', 'конус')
    }
    
    def __init__(self):
        
#        self.show_store()
        pass
    
    @staticmethod
    def show_store():
        
#        for el in Shape.store_fg:
#            print(el, Shape.store_fg[el])
            
        return store_fg
