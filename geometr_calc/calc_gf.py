import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
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
            # xy = change_figure(figure)
            # fig = create_figure(xy[0], xy[1])
            fig = create_figure(figure)
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
        
        @appm.app.route('/change_fig')
        def create_figure(figure):
            if figure == "random":
                coord = Shape.random_figure()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'круг':
                coord = Circle.random_circle()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'квадрат':
                coord = Square.random_square()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'прямоугольник':
                coord = Rect.random_rect()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'треугольник':
                coord = Triang.random_triang()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'трапеция':
                coord = Trapec.random_trapec()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'ромб':
                coord = Rhombe.random_rhombe()
                fig = Shape.create_pfigure(coord[0], coord[1])
            if figure == 'сфера':
                set_fg = Shape.create_vfigure()
                fig = Sphere.random_sphere(set_fg[0], set_fg[1])
            if figure == 'куб':
                set_fg = Shape.create_vfigure()
                fig = Cube.random_cube(set_fg[0], set_fg[1])
            if figure == 'параллелепипед':
                set_fg = Shape.create_vfigure()
                fig = Paralld.random_paralld(set_fg[0], set_fg[1])
            if figure == 'пирамида':
                set_fg = Shape.create_vfigure()
                fig = Pyramd.random_pyramd(set_fg[0], set_fg[1])
            if figure == 'цилиндр':
                set_fg = Shape.create_vfigure()
                fig = Cilind.random_cilind(set_fg[0], set_fg[1])
            if figure == 'конус':
                set_fg = Shape.create_vfigure()
                fig = Conus.random_conus(set_fg[0], set_fg[1])
            return fig

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

        # def create_figure(xs, ys):
        #     fig = Figure()
        #     axis = fig.add_subplot(1, 1, 1)
        #     axis.plot(xs, ys)
        #     return fig
        

if __name__ == "__main__":
    App().app.run(host='0.0.0.0', port=1111, debug=True);