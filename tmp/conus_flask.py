from flask import Flask, Response
import matplotlib.pyplot as plt
import numpy as np
import io
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

app = Flask(__name__)

@app.route('/')
def home():
    return '<img src="plot.png"></img>'

@app.route('/plot.png')
def plot_png():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Определение параметров конуса
    r = 1
    h = 2
    resolution = 50

    # Генерация координат вершин конуса
    theta = np.linspace(0, 2 * np.pi, resolution)
    z = np.linspace(0, h, resolution)
    theta, z = np.meshgrid(theta, z)
    x = r * (h - z) / h * np.cos(theta)
    y = r * (h - z) / h * np.sin(theta)

    # Использование созданных координат для построения поверхности конуса
    ax.plot_surface(x, y, z, alpha=0.7)

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