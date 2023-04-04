from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# Определить символические переменные и функции
var('t C1 C2 C3 C4')
u = Function("u")(t)

# Записать дифференциальное уравнение
de = Eq(u.diff(t, t, t, t) - 3*u.diff(t, t, t) + 3*u.diff(t, t) - u.diff(t), 4*t*exp(t))

# Решить дифференциальное уравнение
sol = dsolve(de, u)
print(sol)

# Подставить начальные условия
ics = {u.subs(t, 0): 2, u.diff(t).subs(t, 0): 3,
       u.diff(t, t).subs(t, 0): -1, u.diff(t, t, t).subs(t, 0): -5}
constants = solve([sol.rhs.subs(ics) - sol.lhs.subs(ics)], [C1, C2, C3, C4])
print(constants)

# Получить окончательное решение
final_sol = sol.subs(constants)
print(final_sol)

# Построить график решения
f = lambdify(t, final_sol.rhs)
t_vals = np.linspace(0, 1, 100)
u_vals = f(t_vals)
plt.plot(t_vals, u_vals)
plt.xlabel('t')
plt.ylabel('u')
plt.show()