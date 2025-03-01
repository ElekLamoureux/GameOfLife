#imports
import sys
import pygame
import random
import copy

#setup
pygame.init()
width = 1000
height = 1000
res = 100
pixilsize = width / res
screen = pygame.display.set_mode((width, height))
screen.fill("white")
clock = pygame.time.Clock()

def update(grid):   
    save = copy.deepcopy(grid)
    for x in range(res):
        for y in range(res):
            count = countn(save, x, y)
            if save[x][y] == 1: # is live
                if count < 2:
                    grid[x][y] = 0
                elif count <= 3:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0
            else: # is dead
                if count == 3:
                    grid[x][y] = 1
    
def countn(grid, x, y):
    if x == 0 or y == 0 or x == res - 1 or y == res - 1:
        return 1
    else:
        return grid[x][y-1] + grid[x][y+1] + \
                grid[x+1][y]+ grid[x+1][y-1] + grid[x+1][y+1] + \
                grid[x-1][y] + grid[x-1][y+1] + grid[x-1][y-1]

#make grid
grid = []
for x in range(res):
    grid.append([])
    for y in range(res):
        #grid[x].append(random.randint(0, 1))
        grid[x].append(0)

grid[1][2] = 1
grid[2][3] = 1
grid[3][1] = 1
grid[3][2] = 1
grid[3][3] = 1
        
running = True

while running:
    for x in range(res):
        for y in range(res):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
                
    update(grid)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        running = False
    dt = clock.tick(5) / 1000
    
    pygame.display.flip()
    
pygame.quit()
