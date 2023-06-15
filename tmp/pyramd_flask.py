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

    # Координаты вершин пирамиды
    vertices = np.array([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0.5, 0.5, 1)])

    # Номера вершин для построения каждой грани
    faces = np.array([(0, 1, 2), (0, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)])

    # Использование созданных списков вершин и граней для построения пирамиды
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='b'))

    # установить размеры осей и названия
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([0,1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=1111)