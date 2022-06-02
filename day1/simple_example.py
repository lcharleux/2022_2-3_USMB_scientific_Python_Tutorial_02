#  A SIMPLE EXAMPLE: A FUNCTION TO PLOT
import numpy as np
import matplotlib.pyplot as plt


def myfunc(x, a=1.0, b=1.0, c=0.0, *args, **kwargs):
    print(f"a={a},b={b},c={c},args={args},kwargs={kwargs}")
    return a * x**2 + b * x + c


x = np.linspace(0.0, 10.0, 11)
y = myfunc(x, c=5)
y2 = myfunc(x, c=2)
 
plt.figure()
i, j = 2, 3
plt.title(f"Matrix: $\\alpha_{{{i}{j}}}$")
plt.grid(which="major", 
      color="k", 
      linestyle="--")
# plt.grid(which="minor", color="gray", linestyle="--")
plt.minorticks_on()
plt.xlabel("Position, $x$")
plt.ylabel("Amplitude, $y$")
from itertools import cycle
my_colors = cycle("rgbcmy")
my_markers = cycle("os*v")
for c in np.arange(10) * 8:
    color = next(my_colors)
    marker = next(my_markers)
    y = myfunc(x, c=c)
    plt.plot(x, y, 
        color = color,
        linewidth=1.0, 
        linestyle="-", 
        label=f"c={c:.2f}", 
        marker = marker)
# plt.xticks(x)
plt.legend(loc="best")
plt.savefig("myfig.png")
plt.close()
# plt.show() # Montre la figure
 