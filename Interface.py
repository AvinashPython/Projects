import pygame
pygame.init()

# Display Dimensions
Height = 600
Width = 600

# Colors
White = (255,255,255)
Black = (0,0,0)

win = pygame.display.set_mode((600,600)) # Window output
pygame.display.set_caption('Sudoku') # name of the window

#intial parameter settings
run = True
mou_pos = None # mouse position

# Grid Size:
# 468*468
# each cell size = 468/9 = 52
grid = 468
CellSize = 468/9
# Functions that we want to be called often.

def events():
    global run, mou_pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseonboard(mou_pos):
                print(mou_pos)


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


# Main program
while run:
    events()
    maindisplay()
    drawboard(win)
    mou_pos = pygame.mouse.get_pos()
    update()

    #pygame.display.update()

pygame.quit()


