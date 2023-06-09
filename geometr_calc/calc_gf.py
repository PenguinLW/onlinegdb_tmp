import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, Response;

from geometr_calc.shapes.shape import Shape


def sapp():
    return App().app

class App():
    def __init__(appm):
        
        appm.app = Flask(__name__);
        
        @appm.app.route("/")
        def app():
            return render_template("app.html", title = 'PenguinL', options = Shape.show_store());
        
        @appm.app.route('/plot.png')
        def plot_png():
            fig = create_figure()
            output = io.BytesIO()
            FigureCanvas(fig).print_png(output)
            return Response(output.getvalue(), mimetype='image/png')
        
        def create_figure():
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)

            xs = list(range(100))
            ys = [random.randint(1, 50) for x in xs]
            # xs = [2, 4, 3, 7]
            # ys = [3, 7, 9, 9]

            xs.append(xs[0])
            ys.append(ys[0])

            axis.plot(xs, ys)
            return fig

if __name__ == "__main__":
    App().app.run(host='0.0.0.0', port=1111, debug=False);