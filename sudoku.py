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
    if num in mat[row] or num in mat[:, col] or num in mat[(row // 3) * 3:(3 + (row // 3) * 3), (col // 3) * 3:(3 + (col // 3) * 3)]:
        return False
    return True

def sudoku_solve(row, col, mat):
    if row==9:
        return True
    if col==9:
        row = row + 1
        col = 0
        return sudoku_solve(row, col, mat)
    if mat[row][col]!=0:
        return sudoku_solve(row,col+1, mat)

    for n in range(1,10):
        if check_correct(n,row, col, mat):
            mat[row][col]=n
            if sudoku_solve(row, col+1, mat):
                return True
            mat[row][col]=0
    return False

sudoku_solve(0,0,sod_main)
print(sod_main)

for i in range(9):
    print(np.sum(sod_main[i]), np.sum(sod_main[:,i]))