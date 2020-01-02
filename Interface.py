import pygame
pygame.init()

# Display Dimensions
Height = 600
Width = 600

# Colors
White = (255,255,255)
Black = (0,0,0)

win = pygame.display.set_mode((600,600))
pygame.display.set_caption('Sudoku')

#intial parameter settings
run = True

# Grid Size:
# 468*468
# each cell size = 468/9 = 52
CellSize = 52


# Main program
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(White)
    pygame.draw.rect(win, Black, (66,100, Width-132, Height-132),2)

    for i in range(9):
        if i%3 ==0:
            pygame.draw.line(win, Black, (66+i*CellSize, 100), (66+i*CellSize, 100+468),2)
            pygame.draw.line(win, Black, (66, 100+i*CellSize),(66+468, 100+i*CellSize),2)
        else:
            pygame.draw.line(win, Black, (66 + i * CellSize, 100), (66 + i * CellSize, 100 + 468))
            pygame.draw.line(win, Black, (66, 100 + i * CellSize), (66 + 468, 100 + i * CellSize))


    pygame.display.update()



pygame.quit()


