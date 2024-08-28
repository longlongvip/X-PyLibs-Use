import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

x = np.linspace(0, 2, 1000)
y = np.sqrt(4 - x*x)

N = 3000
point_x = np.random.rand(N)*(2 - 0)
point_y = np.random.rand(N)*(2 - 0)

point_square_sum = point_x*point_x + point_y*point_y
const_distance = 4.0

point_x_red = point_x[point_square_sum <= const_distance]
point_y_red = point_y[point_square_sum <= const_distance]
point_x_blue = point_x[point_square_sum > const_distance]
point_y_blue = point_y[point_square_sum > const_distance]

N_red = len(point_x_red)
Pro = N_red/N
my_pi = 4.0*Pro

fig, ax = plt.subplots()

line, = ax.plot(x, y)

plt.plot(point_x_red, point_y_red, '.', color='red')
plt.plot(point_x_blue, point_y_blue, '.', color='blue')


plt.axis('scaled')
plt.title('n={} $\pi\\approx${}'.format(N, my_pi))
plt.savefig('Pi的计算.png',bbox_inches='tight',dpi=fig.dpi,pad_inches=0.0)
plt.show()
