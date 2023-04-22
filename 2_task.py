"""
Task:
9. Attēla līmeņu transformācijas, histogrammas operācijas
9b) Izstrādāt datorprogrammu, kas realizē histogrammas vienmērīgošanu.

Author:
Katerina Kuzmina, kk20156

Date:
17.04.2023

For a quick view of the results:
https://gitfront.io/r/user-1975026/cxq5bD8WDEfV/dat-gr-1-sub/
"""

import matplotlib.pyplot as plt
import numpy as np

#   Random number generation
np.random.seed(1)
np.set_printoptions(precision=3)  # Set the number of decimal places
#  mean value of a random variable - 5 and standard deviation - 2
d = np.random.laplace(loc=5, scale=2, size=500)

n, bins, patches = plt.hist(x=d, bins='auto', color='#6161c2', alpha=0.7, rwidth=0.85)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Histogram')

smoothed = np.zeros_like(n)

#   Formula for smoothing
smoothed[0] = (2 * n[0] + n[1]) / 3
smoothed[1:-1] = (n[:-2] + n[1:-1] + n[2:]) / 3
smoothed[-1] = (2 * n[-1] + n[-2]) / 3

plt.plot(bins[:-1], smoothed, color='red')

plt.show()
