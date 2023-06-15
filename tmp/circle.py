import matplotlib.pyplot as plt

circle1 = plt.Circle((0, 0), 0.5, color='r')

fig, ax = plt.subplots()
ax.set_xlim((-1, 1))
ax.set_ylim((-1, 1))
ax.add_artist(circle1)

plt.show()
