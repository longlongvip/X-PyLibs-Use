import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')

x = np.linspace(1, 4, 1000)
y = np.log(x)

N = 3000
point_x = 1 + np.random.rand(N)*(4-1)
point_y = np.random.rand(N)*2

point_log = np.log(point_x)

point_x_red = point_x[point_log >= point_y]
point_y_red = point_y[point_log >= point_y]
point_x_blue = point_x[point_log < point_y]
point_y_blue = point_y[point_log < point_y]
N_red = len(point_x_red)
Pro = N_red/N
res = 6*Pro

fig, ax = plt.subplots()

line, = ax.plot(x, y)

plt.plot(point_x_red, point_y_red, '.', color='red')
plt.plot(point_x_blue, point_y_blue, '.', color='blue')


plt.axis('scaled')
plt.title(f"n={N} $\int_{{1}}^{{4}}\ln(x) dx \\approx${res}")
plt.savefig('积分的计算.png',bbox_inches='tight',dpi=fig.dpi,pad_inches=0.0)
plt.show()
