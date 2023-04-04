import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 0.0005
t = np.linspace(0, seconds_in_year * seconds_in_day * years, frames)


def dif_func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2) = s
    dxdt1 = vx1
    dvxdt1 = - G * m1 * (x1 - x2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5
    dydt1 = vy1
    dvydt1 = G * m1 * (y1 - y2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5

    dxdt2 = vx2
    dvxdt2 = G * m2 * (x2 - x1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5
    dydt2 = vy2
    dvydt2 = - G * m2 * (y2 - y1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5

    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2)


G = 6.67 * 10 ** (-11)

m1 = 3 * 10 ** 5

r1 = 16 * 10 ** 5
x10 = 0
vx10 = (2 * G * m1 / r1) ** 0.5
y10 = r1
vy10 = 6 * 10 ** 8

m2 = 6 * 10 ** 24

x20 = 15 * 10 ** 10
vx20 = - 2000
y20 = 0
vy20 = 1500

s0 = (x10, vx10, y10, vy10,
      x20, vx20, y20, vy20)

sol = odeint(dif_func, s0, t)

fig, ax = plt.subplots()

planet = []
planet_lines = []

for i in range(2):
    planet.append(plt.plot([], [], 'o', color='g'))
    planet_lines.append(plt.plot([], [], '-', color='g'))


def animate(i):
    for j in range(2):
        planet[j][0].set_data(sol[i, 4 * j], sol[i, 4 * j + 2])
        planet_lines[j][0].set_data(sol[:i, 4 * j], sol[:i, 4 * j + 2])


ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 10 * x20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('param_pam_pam.gif')