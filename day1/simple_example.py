#  A SIMPLE EXAMPLE: A FUNCTION TO PLOT
import numpy as np
import matplotlib.pyplot as plt

def myfunc(x, a=1., b=1., c=0., *args, **kwargs):
    print(f"a={a},b={b},c={c},args={args},kwargs={kwargs}")
    return a* x**2 + b* x + c
    
x = np.linspace(0., 10., 11)
y = myfunc(x, c=5)

plt.figure()
plt.title("A nice figure")
plt.grid()
plt.xlabel("Position, $x$")
plt.ylabel("Amplitude, $y$")
plt.plot(x, y)
plt.savefig("myfig.png")
#plt.show() # Montre la figure