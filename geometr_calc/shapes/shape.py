
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

    @staticmethod
    def create_pfigure(xs, ys):
        from matplotlib.figure import Figure
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(xs, ys)
        # установить названия осей
        axis.set_xlabel('X')
        axis.set_ylabel('Y')
        return fig

    @staticmethod
    def create_vfigure():
        from matplotlib.figure import Figure
        fig = Figure()
        axis = fig.add_subplot(111, projection='3d')
        # установить названия осей
        axis.set_xlabel('X')
        axis.set_ylabel('Y')
        axis.set_zlabel('Z')
        return fig, axis;