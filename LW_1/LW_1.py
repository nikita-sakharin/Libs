# Cахарин Н.А. 8О-208Б
# Вариант №15
# ρ = (a * cos(2 * ϕ)) / cos(ϕ), где -π < ϕ < π

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def isfloat(string): # Проверяет можно ли преобразовать строку в float
    try:
        float(string)
        return True
    except ValueError:
        return False

def draw_a_graph(event): # Расчитывает и отрисовывает график функции
    s = ent.get()

    if isfloat(s):
        a = float(s) # Преобразовать строку в функцию
        fig = plt.figure()
        ax = fig.add_subplot(111, projection = 'polar', axisbg = '#FFFFFF')
        step = 0.0005 # Разрешение отрисвки
        indent = 0.2 # Отступ от точек, где знаменатель обращается в 0
        phi0 = np.arange(-np.pi / 2 + indent, np.pi / 2 - indent, step) # первый массив аргументов
        phi1 = np.arange(np.pi / 2 + indent, 3 * np.pi / 2 - indent, step) # второй
        rho0 = a * abs(np.cos(2 * phi0) / np.cos(phi0))
        rho1 = a * abs(np.cos(2 * phi1) / np.cos(phi1))
        ax.plot(phi0, rho0, color = 'green', lw = 2, label = "rho = a * cos(2 * phi) / cos(phi)") # Отобразить первую часть графика
        ax.plot(phi1, rho1, color = 'green', lw = 2) # Вторую
        plt.legend()
        plt.show()
    else:
        lab.configure(text = "Enter a positive float") # Вывести уведомление

root = Tk() # Основное окно
lab = Label( # Подпись к графику
    root,
    text = "Input coefficient 'a' in expression\n rho = a * cos(2 * phi) / cos(phi)",
    font = "Arial 16",
    fg = "blue"
)

ent = Entry( # Окошечко для ввода аргумента
    root,
    width = 20,
    bd = 3
)

but = Button( # Кнопка
    root,
    text = "Построить график",
    bg = "lightgreen"
)

but.bind("<Button-1>", draw_a_graph)
root.bind("<Return>", draw_a_graph)

lab.pack()
ent.pack()
but.pack()

root.mainloop()
