from tkinter import *
import math
import numpy as np

import matplotlib.path as mplPath

def callback(event):
    for j in range(n):
        for i in range(n):
            poly = mplPath.Path(np.array([ [Array[j][i][0], Array[j][i][1]],
                                           [Array[j][i][0], Array[j][i][1]],
                                           [Array[j][i][2], Array[j][i][3]],
                                           [Array[j][i][4], Array[j][i][5]],
                                           [Array[j][i][6], Array[j][i][7]],
                                           [Array[j][i][8], Array[j][i][9]],
                                           [Array[j][i][10],Array[j][i][11]]]))
            if poly.contains_point((event.x, event.y)) == 1:
                points = list(Array[j][i])
                w.create_polygon(points, outline=python_green, fill=python_green, width=6)
                return

# zum testen ist n == 5
n = 8

Array = np.zeros((n,n,12))

master = Tk()
canvas_width = 800
canvas_height =800
python_green = "#476042"
w = Canvas(master,width=canvas_width,height=canvas_height)
w.pack()


# kann übergeben werden
edge_length = 50
points = []

# breite von Hexo ermitteln
xs = []
ys = []
y = 0
x = 0
for angle in range(0, 360, 60):
    y += math.cos(math.radians(angle)) * edge_length
    ys.append(y)
    x += math.sin(math.radians(angle)) * edge_length
    xs.append(x)

y_top =(max(ys))
x_right = (max(xs))


for j in range(n):
    for i in range(n):
        x =40+ x_right*i + x_right/2*j
        y = 50 + y_top*j
        points = []
        k = 0
        for angle in range(0, 360, 60):
            y +=math.cos(math.radians(angle)) * edge_length
            x +=math.sin(math.radians(angle)) * edge_length
            points.append(x)
            points.append(y)
            Array[j][i][k] = x
            Array[j][i][k+1] = y
            k += 2

        w.create_polygon(points, outline=python_green,fill='yellow', width=3)

w.bind("<Button-1>", callback)


master.mainloop()


warte = 1

















