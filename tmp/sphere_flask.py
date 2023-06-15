#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#import numpy as np
#from flask import Flask, render_template_string, Response
#
#app = Flask(__name__)
#
#u = np.linspace(0, 2 * np.pi, 100)
#v = np.linspace(0, np.pi, 100)
#
#x = 2 * np.outer(np.cos(u), np.sin(v))
#y = 2 * np.outer(np.sin(u), np.sin(v))
#z = 2 * np.outer(np.ones(np.size(u)), np.cos(v))
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, z)
#
#@app.route('/')
#def index():
#    return render_template_string('< src="/plot.png" />')
#
#@app.route('/plot.png')
#def plot_png():
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')
#
#if __name__ == '__main__':
#    app.run(debug=True, port=1111)


from flask import Flask, render_template, Response
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '<img src="plot.png"></img>'

@app.route('/plot.png')
def plot_png():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = 2 * np.outer(np.cos(u), np.sin(v))
    y = 2 * np.outer(np.sin(u), np.sin(v))
    z = 2 * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z)

    # установить размеры осей и названия
    # ax.set_xlim([0,1])
    # ax.set_ylim([0,1])
    # ax.set_zlim([0,1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=1111)
