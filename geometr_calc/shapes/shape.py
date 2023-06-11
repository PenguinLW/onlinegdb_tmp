
class Shape:
    store_fg = {
        'плоскость': ('круг', 'квадрат', 'прямоугольник', 'треугольник', 'трапеция', 'ромб'),
        'объём': ('сфера', 'куб', 'параллелепипед', 'пирамида', 'цилиндр', 'конус')
    }
    
    def __init__(self):
        
#        self.show_store()
        pass
    
    @staticmethod
    def show_store():
        
#        for el in Shape.store_fg:
#            print(el, Shape.store_fg[el])
        return Shape.store_fg
    
    @staticmethod
    def random_figure():
        import random
        xs = list(range(random.randint(1, 100)))
        ys = [random.randint(1, 50) for x in xs]
        # xs = [2, 4, 3, 7]
        # ys = [3, 7, 9, 9]
        xs.append(xs[0])
        ys.append(ys[0])
        return xs, ys
