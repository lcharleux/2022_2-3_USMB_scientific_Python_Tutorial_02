# SUDOKU SOLVER AND MAYBE MORE !

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_csv_grid(path):
    return pd.read_csv(path, header= None).values

def get_next_move(data):
    N = set(np.arange(1,10)) # Allowed numbers
    best_len = 9
    flag = 1
    for r,c in np.array(np.where(data == 0)).T:
        #r,c = 4,2 # ROW, COL
        R = set(data[r]) # ROW SET
        C = set(data[:, c]) # COL SET
        rb = (r//3)*3 # = r - r%3
        rc = (c//3)*3
        B = set(data[rb:rb+3,rc:rc+3].flatten())
        P = N - R - C - B
        lp = len(P)
        if lp < best_len:
            best_len = lp
            best_combination = r, c, P 
        if lp == 1:
            flag = 0
            break
        elif lp == 0:
            flag = 2
            break
    return flag, best_combination


path = "sudoku_000.csv"
data = read_csv_grid(path)
flag, best_combination = get_next_move(data)
r, c, P = best_combination
print(f"flag={flag}, r={r}, c={c}, P = {P}")
