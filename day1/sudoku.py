# SUDOKU SOLVER AND MAYBE MORE !

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def read_csv_grid(path):
    return pd.read_csv(path, header= None).values

def get_next_move(data):
    N = set(np.arange(1,10)) # Allowed numbers
    best_len = 10
    heatmap = np.zeros_like(data) * np.nan
    for r,c in np.array(np.where(data == 0)).T:
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

def plot_grid(data):
    if 0 in data:
        flag, best_combination, heatmap = get_next_move(data)
        r, c, P = best_combination
        title = f"flag={flag}, r={r}, c={c}, P = {P}"
    else:
        title = "FINISHED !!!"
        heatmap = np.zeros_like(data) * np.nan

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    plt.xticks(range(9), [f"C{v+1}" for v in range(9)])
    plt.yticks(range(9), [f"R{v+1}" for v in range(9)])
    #plt.minorticks_on()
    props = dict(boxstyle='round', facecolor="white", alpha=0.5)
    plt.title(title)
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

def check_grid(grid):
    flag = 0
    for i in range(9):
        #ROW
        v = grid[i]
        v = v[v != 0]
        s = set(v)
        if len(s) !=  v.size:
            print(f"Row {i} wrong")
            flag = 1
        v = grid[:, i]
        v = v[v != 0]
        s = set(v)
        if len(s) !=  v.size:
            print(f"Col {i} wrong")
            flag = 1        
        row = i // 3
        col = i % 3
        v = grid[row * 3 : row * 3 + 3, 
                 col * 3 : col * 3 + 3]
        v = v.flatten()
        v = v[v != 0]
        s = set(v)
        if len(s) !=  v.size:
            print(f"Block {row}{col} wrong")
            flag = 1           
    if flag == 0:
        print("GRID OK !")
    return flag    

class SudokuSolver:
    """
    Solves sudoku.
    """
    def __init__(self, path):
        grid = read_csv_grid(path)
        self.grid = grid

    def plot(self):
        plot_grid(self.grid)    

    def is_finished(self):
        return not 0 in self.grid   

    def play_one_turn(self):
        if not self.is_finished():
            flag, best_combination, heatmap = get_next_move(self.grid)
            r, c, P = best_combination
            if flag == 0:
                self.grid[r,c] = P.pop()
                return True
            elif flag == 1:
                self.grid[r,c] = random.sample(P, 1)[0]
                return True
            else:
                return False
        else:
            print("Finished !")
            return False
    def solve(self):
        iter = 0
        play_again = True
        while play_again:
            iter +=  1
            success = self.play_one_turn()
            if not success: 
                play_again = False 
        print(f"Iterations: {iter}")

    def check(self):
        return check_grid(self.grid)

#path = "sudoku_000.csv"
path = "sudoku_extreme.csv"
sudoku = SudokuSolver(path)
#sudoku.grid *=0
sudoku.solve()
sudoku.check()
sudoku.plot()