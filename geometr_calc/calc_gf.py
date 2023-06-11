import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, Response;

from shapes.shape import Shape
from shapes.p_shapes import *
from shapes.v_shapes import *


# def sapp():
#     return App().app

class App():
    def __init__(appm):
        
        appm.app = Flask(__name__);
        
        @appm.app.route("/")
        def app():
            return render_template("app.html", title = 'PenguinL', options = Shape.show_store());

        @appm.app.route('/-/plot.png')
        @appm.app.route('/plot.png')
        def plot_png(figure="random"):
            xy = change_figure(figure)
            fig = create_figure(xy[0], xy[1])
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
        
        @appm.app.route('/change_fig')
        def change_figure(figure):
            if figure == "random":
                xy = Shape.random_figure()
            if figure == 'круг':
                xy = Circle.random_circle()
            if figure == 'квадрат':
                xy = Square.random_square()
            if figure == 'прямоугольник':
                xy = Rect.random_rect()
            if figure == 'треугольник':
                xy = Triang.random_triang()
            if figure == 'трапеция':
                xy = Trapec.random_trapec()
            if figure == 'ромб':
                xy = Rhombe.random_rhombe()
            if figure == 'сфера':
                xy = Sphere.random_sphere()
            if figure == 'куб':
                xy = Cube.random_cube()
            if figure == 'параллелепипед':
                xy = Paralld.random_paralld()
            if figure == 'пирамида':
                xy = Pyram.random_pyram()
            if figure == 'цилиндр':
                xy = Cilinder.random_cilinder()
            if figure == 'конус':
                xy = Conus.random_conus()
            return xy

        @appm.app.route('/show_store')
        def show_store():

            return Shape.show_store()

        @appm.app.route('/p1/plot.png', methods=['GET', 'POST'])
        def circle_png(figure=Shape.show_store()['плоскость'][0]):
            return plot_png(figure)
        @appm.app.route('/p2/plot.png')
        def square_png(figure=Shape.show_store()['плоскость'][1]):
            return plot_png(figure)
        @appm.app.route('/p3/plot.png')
        def rect_png(figure=Shape.show_store()['плоскость'][2]):
            return plot_png(figure)
        @appm.app.route('/p4/plot.png')
        def triang_png(figure=Shape.show_store()['плоскость'][3]):
            return plot_png(figure)
        @appm.app.route('/p5/plot.png')
        def trapec_png(figure=Shape.show_store()['плоскость'][4]):
            return plot_png(figure)
        @appm.app.route('/p6/plot.png')
        def rhombe_png(figure=Shape.show_store()['плоскость'][5]):
            return plot_png(figure)

        @appm.app.route('/v1/plot.png')
        def sphere_png(figure=Shape.show_store()['объём'][0]):
            return plot_png(figure)
        @appm.app.route('/v2/plot.png')
        def cube_png(figure=Shape.show_store()['объём'][1]):
            return plot_png(figure)
        @appm.app.route('/v3/plot.png')
        def paralld_png(figure=Shape.show_store()['объём'][2]):
            return plot_png(figure)
        @appm.app.route('/v4/plot.png')
        def pyram_png(figure=Shape.show_store()['объём'][3]):
            return plot_png(figure)
        @appm.app.route('/v5/plot.png')
        def cilinder_png(figure=Shape.show_store()['объём'][4]):
            return plot_png(figure)
        @appm.app.route('/v6/plot.png')
        def conus_png(figure=Shape.show_store()['объём'][5]):
            return plot_png(figure)

        def create_figure(xs, ys):
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(xs, ys)
            return fig
        

if __name__ == "__main__":
    App().app.run(host='0.0.0.0', port=1111, debug=True);
