import numpy as np
# Sudoku puzzle to solve
sod_main = np.array([[0,2,0,0,7,0,1,9,0],
                     [1,3,0,0,0,0,0,5,8],
                     [4,9,0,0,0,3,0,0,2],
                     [8,1,0,0,4,0,0,0,0],
                     [0,4,9,6,0,5,8,2,0],
                     [0,0,0,0,3,0,0,4,1],
                     [9,0,0,4,0,0,0,3,6],
                     [2,6,0,0,0,0,0,8,9],
                     [0,7,3,0,9,0,0,1,0]])
#print(sod_main)

def check_correct(num, row, col, mat):
    ''' Function to check if a number (num) is okay to be kept in row and col of the sudoku puzzle (mat)'''
    if n in mat[i] or n in mat[:, j] or n in mat[(i // 3) * 3:(3 + (i // 3) * 3), (j // 3) * 3:(3 + (j // 3) * 3)]:
        return False
    return True

