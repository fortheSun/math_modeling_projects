from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Создание пространства для анимации
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

seconds_in_year = 365 * 24 * 60 * 60
years = 1

frames = 365
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1, z1, v_z1,
     x2, v_x2, y2, v_y2, z2, v_z2,
     x3, v_x3, y3, v_y3, z3, v_z3,
     x4, v_x4, y4, v_y4, z4, v_z4) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * m_hole * x1 / (x1**2 + y1**2 + z1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m_hole * y1 / (x1**2 + y1**2 + z1**2)**1.5
    dzdt1 = v_z1
    dv_zdt1 = - G * m_hole * z1 / (x1**2 + y1**2 + z1**2)**1.5

    dxdt2 = v_x2
    dv_xdt2 = - G * m_hole * x2 / (x2**2 + y2**2 + z2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * m_hole * y2 / (x2**2 + y2**2 + z2**2)**1.5
    dzdt2 = v_z2
    dv_zdt2 = - G * m_hole * z2 / (x2**2 + y2**2 + z2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = - G * m_hole * x3 / (x3**2 + y3**2 + z3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = - G * m_hole * y3 / (x3**2 + y3**2 + z3**2)**1.5
    dzdt3 = v_z3
    dv_zdt3 = - G * m_hole * z3 / (x3**2 + y3**2 + z3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = - G * m_hole * x4 / (x4**2 + y4**2 + z4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - G * m_hole * y4 / (x4**2 + y4**2 + z4**2)**1.5
    dzdt4 = v_z4
    dv_zdt4 = - G * m_hole * z4 / (x4**2 + y4**2 + z4**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1, dzdt1, dv_zdt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2, dzdt2, dv_zdt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3, dzdt3, dv_zdt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4, dzdt4, dv_zdt4)

G = 6.67 * 10**(-11)

m_hole = 25 * 10**29
# m_hole = 2 * 10**30

x0_earth = 149 * 10**9
v_x0_earth = 0
y0_earth = 0
v_y0_earth = 30000
z0_earth = 0
v_z0_earth = 0

x0_mercury = 0
v_x0_mercury = -47360
y0_mercury = 0.38709927 * 149 * 10**9
v_y0_mercury = 0
z0_mercury = 0
v_z0_mercury = 0

x0_venus = -0.723332 * 149 * 10**9
v_x0_venus = 0
y0_venus = 0
v_y0_venus = -35020
z0_venus = 0
v_z0_venus = 0

x0_mars = 0
v_x0_mars = -24077
y0_mars = 1.523662 * 149 * 10**9
v_y0_mars = 0
z0_mars = 0
v_z0_mars = 0

s0 = (x0_earth, v_x0_earth, y0_earth, v_y0_earth, z0_earth, v_z0_earth,
      x0_mercury, v_x0_mercury, y0_mercury, v_y0_mercury, z0_mercury, v_z0_mercury,
      x0_venus, v_x0_venus, y0_venus, v_y0_venus, z0_venus, v_z0_venus,
      x0_mars, v_x0_mars, y0_mars, v_y0_mars, z0_mars, v_z0_mars)

sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        z1 = sol[i, 4]
        x2 = sol[i, 6]
        y2 = sol[i, 8]
        z2 = sol[i, 10]
        x3 = sol[i, 12]
        y3 = sol[i, 14]
        z3 = sol[i, 16]
        x4 = sol[i, 18]
        y4 = sol[i, 20]
        z4 = sol[i, 22]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        z1 = sol[:i, 4]
        x2 = sol[:i, 6]
        y2 = sol[:i, 8]
        z2 = sol[:i, 10]
        x3 = sol[:i, 12]
        y3 = sol[:i, 14]
        z3 = sol[:i, 16]
        x4 = sol[:i, 18]
        y4 = sol[:i, 20]
        z4 = sol[:i, 22]

    return ((x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4))


ball1 = ax.plot([], [], [], 'o', color='lightblue')[0]
line1 = ax.plot([], [], [], '-', color='lightblue')[0]

ball2 = ax.plot([], [], [], 'o', color='r')[0]
line2 = ax.plot([], [], [], '-', color='r')[0]

ball3 = ax.plot([], [], [], 'o', color='darksalmon')[0]
line3 = ax.plot([], [], [], '-', color='darksalmon')[0]

ball4 = ax.plot([], [], [], 'o', color='lightcoral')[0]
line4 = ax.plot([], [], [], '-', color='lightcoral')[0]

ax.scatter([0], [0], [0], color='darkslateblue', s=200)


# Функция подстановки координат в анимируемые объекты
def animate(i):
    points1, points2, points3, points4 = solve_func(i, 'point')
    lpoints1, lpoints2, lpoints3, lpoints4 = solve_func(i, 'line')

    ball1.set_data([points1[0]], [points1[1]])
    ball1.set_3d_properties([points1[2]])

    line1.set_data(lpoints1[0], lpoints1[1])
    line1.set_3d_properties(lpoints1[2])

    ball2.set_data([points2[0]], [points2[1]])
    ball2.set_3d_properties([points2[2]])

    line2.set_data(lpoints2[0], lpoints2[1])
    line2.set_3d_properties(lpoints2[2])

    ball3.set_data([points3[0]], [points3[1]])
    ball3.set_3d_properties([points3[2]])

    line3.set_data(lpoints3[0], lpoints3[1])
    line3.set_3d_properties(lpoints3[2])

    ball4.set_data([points4[0]], [points4[1]])
    ball4.set_3d_properties([points4[2]])

    line4.set_data(lpoints4[0], lpoints4[1])
    line4.set_3d_properties(lpoints4[2])


# Украшательсвта и масштабирование
edge = 1 * x0_earth
ax.set_xlim3d([-edge, edge])
# ax.set_xlabel('X')

ax.set_ylim3d([-edge, edge])
# ax.set_ylabel('Y')

ax.set_zlim3d([-edge, edge])
# ax.set_zlabel('Z')

# ax = Axes3D(fig)
ax.xaxis.set_pane_color('black')
ax.yaxis.set_pane_color('black')
ax.zaxis.set_pane_color('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.style.use('dark_background')
ax.set_facecolor('black')
# Анимирование
ani = FuncAnimation(fig, animate, frames=frames, interval=50)

ani.save('3D_motion_test3.gif')