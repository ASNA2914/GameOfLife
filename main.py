import pygame
import random
import sys

from CFG import *

rows = GetConfig(4)
cols = GetConfig(4)
resolution = GetConfig(3)
w = cols * resolution
h = rows * resolution
grid = GetConfig(5)
DeadColor = GetConfig(1)
LiveColor = GetConfig(2)

def createGrid(generated : bool):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(cols):
        for j in range(rows):
            if generated:
                grid[i][j] = random.randint(0,1)
            else:
                grid[i][j] = 0
    return grid

def print_grid(grid):
    for _ in grid:
        for i in _:
            print(i,end=" ")
        print()

def draw():
    global g
    pygame.display.flip()
    win.fill((0,0,0))
    for i in range(cols):
        for j in range(rows):
            color = (0,0,0)
            if g[i][j] == 0:
                color = DeadColor
            if g[i][j] == 1:
                color = LiveColor
            if grid:
                pygame.draw.rect(win, color, (i*resolution, j*resolution, resolution-1, resolution-1))
            elif not grid:
                pygame.draw.rect(win, color, (i*resolution, j*resolution, resolution, resolution))
    next_g = createGrid(False)
    for i in range(-1,cols-1):
        for j in range(-1,rows-1):
            neigbors = checkNeighbors(g, i, j)
            state = g[i][j]
            if (state == 0 and neigbors == 3):
                next_g[i][j] = 1
            elif(state == 1 and (neigbors < 2 or neigbors > 3)):
                next_g[i][j] = 0 
            else:
                next_g[i][j] = state
    if not pause:
        g = next_g


def checkNeighbors(grid,x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            count += grid[x+i][y+j]
    count -= grid[x][y]
    return count

pygame.init()
win = pygame.display.set_mode((w,h))
g = createGrid(False)
pause = False
clock = pygame.time.Clock()
run = True

while run:
    m_pos_x, m_pos_y = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if pause == False:
                    pause = True
                else:
                    pause = False
            if e.key == pygame.K_d:
                g[int(m_pos_x/resolution)][int(m_pos_y/resolution)] = 1
            if e.key == pygame.K_e:
                g[int(m_pos_x/resolution)][int(m_pos_y/resolution)] = 0
            if e.key == pygame.K_g:
                g = createGrid(True)
            if e.key == pygame.K_f:
                g = createGrid(False)
            if e.key == pygame.K_n and pause:
                next_g = createGrid(False)
                for i in range(-1,cols-1):
                    for j in range(-1,rows-1):
                        neigbors = checkNeighbors(g, i, j)
                        state = g[i][j]
                        if (state == 0 and neigbors == 3):
                            next_g[i][j] = 1
                        elif(state == 1 and (neigbors < 2 or neigbors > 3)):
                            next_g[i][j] = 0 
                        else:
                            next_g[i][j] = state
                g = next_g
            if e.key == pygame.K_F2:
                pygame.image.save(win, "screenshot.jpg")
            if e.key == pygame.K_F3:
                Save(g)
            if e.key == pygame.K_F4:
                g = Load(g)
    draw()
    clock.tick(30)