# SUDOKU SOLVER AND MAYBE MORE !

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_csv_grid(path):
    return pd.read_csv(path, header= None).values

def get_next_move(data):
    N = set(np.arange(1,10)) # Allowed numbers
    best_len = 9
    heatmap = np.zeros_like(data) * np.nan
    for r,c in np.array(np.where(data == 0)).T:
        #r,c = 4,2 # ROW, COL
        R = set(data[r]) # ROW SET
        C = set(data[:, c]) # COL SET
        rb = (r//3)*3 # = r - r%3
        rc = (c//3)*3
        B = set(data[rb:rb+3,rc:rc+3].flatten())
        P = N - R - C - B
        lp = len(P)
        heatmap[r,c] = lp
        if lp < best_len:
            best_len = lp
            best_combination = r, c, P 
        
    if best_len == 0:
        flag = 2
    elif best_len == 1:
        flag = 0
    else:
        flag = 1         
    return flag, best_combination, heatmap


path = "sudoku_000.csv"
data = read_csv_grid(path)
flag, best_combination, heatmap = get_next_move(data)
r, c, P = best_combination
print(f"flag={flag}, r={r}, c={c}, P = {P}")


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xticks(range(9), [f"C{v+1}" for v in range(9)])
plt.yticks(range(9), [f"R{v+1}" for v in range(9)])
#plt.minorticks_on()
props = dict(boxstyle='round', facecolor="white", alpha=0.5)
plt.imshow(heatmap, cmap = "jet", alpha = 1.)
for i in range(9):
    for j in range(9):
        if data[j, i] == 0:
            ax.text(i, j, str(int(heatmap[j,i])), va='center', ha='center', 
                color = "black", bbox = props)

        else:
            ax.text(i, j, str(data[j,i]), va='center', ha='center', color = "black")
plt.colorbar()
plt.show()