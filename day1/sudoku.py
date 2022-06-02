# SUDOKU SOLVER AND MAYBE MORE !

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = "sudoku_000.csv"
data = pd.read_csv(path, header= None).values

N = set(np.arange(1,10)) # Allowed numbers
# CASE 1: 0,0
r,c = 4,2 # ROW, COL
R = set(data[r]) # ROW SET
C = set(data[:, c]) # COL SET
rb = (r//3)*3 # = r - r%3
rc = (c//3)*3
B = set(data[rb:rb+3,rc:rc+3].flatten())
