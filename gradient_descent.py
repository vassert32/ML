# -*- coding: utf-8 -*-
"""gradient_descent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19kw4pekXP0N9Qrn0ay_umasW-M2oxMB_
"""

import time
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x*x - 5*x + 5

def df(x):
    return 2*x - 5

N = 20          # число итераций
xx = 0          # начальное значение
lmd = 0.9       # шаг сходимости

x_plt = np.arange(0, 5, 0.1)        # для отрисовки графика ось х
y_plt = [func(x) for x in x_plt]    # для отрисовки графика ось у

plt.ion()                   # включение интерактивного режима отображения графиков
fig, ax = plt.subplots()    # создание окна и осей для графика
ax.grid(True)               # отображение сетки на графике

ax.plot(x_plt, y_plt)                       # отображение параболы
point = ax.scatter(xx, func(xx), c='red')   # начальное отображение точки

for i in range(N):
    xx = xx - lmd*df(xx)                # изменение аргумента по формуле спуска градиента

    point.set_offsets([xx, func(xx)])   # отрисовка нового положения точки

    # перерисовка графика и задержка на 20 мс
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()   # выключение интерактивного режима отображения графиков

print(xx)
ax.scatter(xx, func(xx), c='blue')
plt.show()