import pygame

# Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
FRAMERATE = 500


# classes

class Ball:
    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        global bgColor, fgColor, BORDER, HEIGHT, WIDTH

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + Ball.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER + Ball.RADIUS or newy > HEIGHT - BORDER - Ball.RADIUS:
            self.vy = -self.vy
        elif newx + Ball.RADIUS > WIDTH - Paddle.WIDTH and abs(newy - paddle.y) < Paddle.HEIGHT // 2:
            self.vx = - self.vx

        else:
            self.show(bgColor)
            self.x = newx
            self.y = newy
            self.show(fgColor)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen, WIDTH, HEIGHT
        pygame.draw.rect(screen, color, pygame.Rect((WIDTH - self.WIDTH, self.y - self.HEIGHT // 2),
                                                    (self.WIDTH, self.HEIGHT)))

    def update(self):
        global BORDER, HEIGHT, WIDTH
        newY = pygame.mouse.get_pos()[1]

        if newY - Paddle.HEIGHT // 2 > BORDER and newY + Paddle.HEIGHT // 2 < HEIGHT - BORDER:
            print(newY)
            self.show(pygame.Color("black"))
            self.y = newY
            self.show(pygame.Color("white"))


# Draw the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bgColor = pygame.Color("black")
fgColor = pygame.Color("white")

screen.fill(bgColor)

pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (WIDTH, BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))

ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT // 2, -VELOCITY, -VELOCITY)
ball.show(fgColor)

paddle = Paddle(HEIGHT // 2)
paddle.show(fgColor)

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)

    pygame.display.flip()
    paddle.update()
    ball.update()

pygame.quit()
