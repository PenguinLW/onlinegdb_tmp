import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, Response;

from shapes.shape import Shape
from shapes.p_shapes import Circle
from shapes.p_shapes import Square


# def sapp():
#     return App().app

class App():
    def __init__(appm):
        
        appm.app = Flask(__name__);
        
        @appm.app.route("/")
        def app():
            return render_template("app.html", title = 'PenguinL', options = Shape.show_store());
        
        @appm.app.route('/plot.png')
        def plot_png():
            xy = change_figure()
            fig = create_figure(xy[0], xy[1])
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
        
        @appm.app.route('/change_fig')
        def change_figure():
            xy = Shape.random_figure()
            # xy = Circle.random_circle()
            # xy = Square.random_square()
            return xy
        
        def create_figure(xs, ys):
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(xs, ys)
            return fig
        

if __name__ == "__main__":
    App().app.run(host='0.0.0.0', port=1111, debug=True);
