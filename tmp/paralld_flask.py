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

    # Создание списка вершин параллелепипеда
    vertices = np.array([(0, 0, 0),
                         (1, 0, 0),
                         (1, 1, 0),
                         (0, 1, 0),
                         (0, 0, 1),
                         (1, 0, 1),
                         (1, 1, 1),
                         (0, 1, 1)])

    # Создание списка граней параллелепипеда
    faces = np.array([(0, 1, 2, 3),
                      (0, 1, 5, 4),
                      (1, 2, 6, 5),
                      (2, 3, 7, 6),
                      (3, 0, 4, 7),
                      (4, 5, 6, 7)])

    # Использование созданных списков вершин и граней для построения параллелепипеда
    ax.add_collection3d(
        Poly3DCollection([vertices[face] for face in faces], alpha=.25, facecolor='b')
    )
    # Настройка параметроврафика
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
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