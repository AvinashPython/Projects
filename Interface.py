import pygame
import numpy as np
import time
from sudoku import check_correct, sudoku_solve
pygame.init()

sudoku = np.array([[0,2,0,0,7,0,1,9,0],
                   [1,3,0,0,0,0,0,5,8],
                   [4,9,0,0,0,3,0,0,2],
                   [8,1,0,0,4,0,0,0,0],
                   [0,4,9,6,0,5,8,2,0],
                   [0,0,0,0,3,0,0,4,1],
                   [9,0,0,4,0,0,0,3,6],
                   [2,6,0,0,0,0,0,8,9],
                   [0,7,3,0,9,0,0,1,0]])

# to identify the positions that are filled so that it is not changed in the game
filled_list = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            filled_list.append((i,j))

print(filled_list)
# Display Dimensions
Height = 600
Width = 600

# Colors
White = (255,255,255)
Black = (0,0,0)
Red = (200,0,0)
Dark_red = (255,0,0)
Green = (0,200,0)
Dark_green = (0,255,0)

#intial parameter settings
run = True
mou_pos = None # mouse position
selected = None
key = None
start =  time.time()
# Grid Size:
# 468*468
# each cell size = 468/9 = 52
grid = 468
CellSize = 468/9
# Functions that we want to be called often.

def events():
    global run, mou_pos, key, sudoku, selected, filled_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 257:
                #print('atleast this works')
                key = 1
            if event.key == 258:
                key = 2
            if event.key == 259:
                key = 3
            if event.key == 260:
                key = 4
            if event.key == 261:
                key = 5
            if event.key == 262:
                key = 6
            if event.key == 263:
                key = 7
            if event.key == 264:
                key = 8
            if event.key == 265:
                key = 9
            print(key)
            if sudoku[int(selected[1])][int(selected[0])]==0:
                if check_correct(key, int(selected[1]), int(selected[0]), sudoku):
                    sudoku[int(selected[1])][int(selected[0])] = key
                else:
                    font = pygame.font.SysFont(None, 30)
                    print('Wrong Value')
                    text = font.render('X Check Again!', True, Red)
                    win.blit(text, (66,50))

            if event.key == pygame.K_BACKSPACE:
                print('Backspace')
                pos = (int(selected[1]), int(selected[0]))
                print(pos)
                if pos not in filled_list:
                    print('inside if',pos[0],pos[1])
                    sudoku[pos[0]][pos[1]] = 0
                    key = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            select = mouseonboard(mou_pos)
            if select:
                selected = select
                print(selected)
    #pygame.display.update()


def maindisplay():
    ''' for drawing the main window'''
    win.fill(White)
    #pygame.display.update()

def drawboard(window):
    ''' for drawing the grid on output window'''
    pygame.draw.rect(win, Black, (66, 100, Width - 132, Height - 132), 2)
    for i in range(9):
        if i%3 ==0:
            pygame.draw.line(window, Black, (66+i*CellSize, 100), (66+i*CellSize, 100+468),2)
            pygame.draw.line(window, Black, (66, 100+i*CellSize),(66+468, 100+i*CellSize),2)
        else:
            pygame.draw.line(window, Black, (66 + i * CellSize, 100), (66 + i * CellSize, 100 + 468))
            pygame.draw.line(window, Black, (66, 100 + i * CellSize), (66 + 468, 100 + i * CellSize))

def update():
    pygame.display.update()

def mouseonboard(pos):
    if pos[0] < 66 or pos[0]>66+grid or pos[1]>100+grid or pos[1]<100:
        return False
    return (((pos[0]-66)//CellSize), ((pos[1]-100)//CellSize))

def displaygame( board, time):
    font = pygame.font.SysFont(None,30)
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                text = font.render(str(board[i][j]), True, Black)
                win.blit(text, ((66+(CellSize/2-text.get_width()/2 )+j*CellSize), (100+(CellSize/2-text.get_width()/2)+i*CellSize)))

    time_text = font.render('Time:'+ format_time(time), True, Black)
    win.blit(time_text, (400, 70))

def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def button(txt, c1, c2, x, y , w, h ):
    global mou_pos, win

    font = pygame.font.SysFont(None, 30)
    click = pygame.mouse.get_pressed()

    if x+w > mou_pos[0] > x and y+h > mou_pos[1] > y:
        pygame.draw.rect(win, c1, (x,y,w,h))
        if click[0]==1 and txt == 'Clear':
            #print('Gotta Clear')
            clear()
        elif click[0]==1 and txt == 'Solve':
            #print('Gotta Solve')
            clear()
            sudoku_solve(0,0,sudoku)
    else:
        pygame.draw.rect(win, c2, (x, y, w, h))
    text_surf = font.render(txt, True, Black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x+(w/2)),(y+(h/2)))
    win.blit(text_surf, text_rect)

def clear():
    global sudoku, filled_list

    for i in range(9):
        for j in range(9):
            if (i,j) not in filled_list:
                sudoku[i][j]=0

# Main program
win = pygame.display.set_mode((600, 600))  # Window output
pygame.display.set_caption('Sudoku') # name of the window
clock = pygame.time.Clock()
while run:
    play_time = round(time.time() - start)

    maindisplay()
    drawboard(win)
    events()
    mou_pos = pygame.mouse.get_pos()
    displaygame(sudoku,play_time)
    button('Clear', Dark_green, Green,  350, 30, 75, 30)
    button('Solve', Dark_green, Green, 450, 30, 75, 30)

    update()
    clock.tick(5)


    #pygame.display.update()

pygame.quit()


print('Avi')