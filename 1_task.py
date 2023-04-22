"""
Task:
1. Datora formētā attēla uzbūve, informatīvais saturs un uztvere
1a) Izstrādāt datorprogrammu attāla krāsu komponenšu
vizualizācijai divu argumentu funkciju grafiku veidā.
Jāuzzīmē virsma 3D telpā, kas satāv no punktiem (x,y,z) tādiem,
kur z ir attēla punkta (x,y) krāsas komponentes vērtība.

Author:
Katerina Kuzmina, kk20156

Date:
13.04.2023

For a quick view of the results:
https://gitfront.io/r/user-1975026/cxq5bD8WDEfV/dat-gr-1-sub/
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image = Image.open("blue_circle_3.jpg")
pixels = image.load()  # list with pixels
x, y = image.size  # Height and width of an image

image_size_x = x
image_size_y = y

array = []

for i in range(x):
    for j in range(y):

        color = pixels[i, j]  # list with color values
        value = color[0] * 0.3 + color[1] * 0.59 + color[2] * 0.11  # The luminance of each color
        array.append([i, j, value])

x_ax = np.array([])
y_ax = np.array([])
z_ax = np.array([])

length = len(array)

for x in range(length):
    x_ax = np.append(x_ax, array[x][0])
    y_ax = np.append(y_ax, array[x][1])
    z_ax = np.append(z_ax, array[x][2])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

z_pos = 0
dx = dy = np.ones_like(z_pos)

#   Generating bars (dx, dy z_ax - width, depth, height of each bar.
#   x_ax, y_ax - x and y coordinates of each bar)
ax.bar3d(x_ax, y_ax, 0, dx, dy, z_ax, zsort='average')

plt.show()
