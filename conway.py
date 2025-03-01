#imports
import pygame
import random

#setup
pygame.init()
width = 1000
height = 1000
res = 10
pixilsize = width / res
screen = pygame.display.set_mode((width, height))
screen.fill("white")
clock = pygame.time.Clock()

grid = []



def update(grid):
    save = grid
    for x in range(res):
        for y in range(res):
            if save[x][y] == 1:
                if countn(grid, x, y) < 2:
                    grid[x][y] = 0
                elif countn(save, x, y) <= 3:
                    grid[x][y] = 1
                elif countn(save, x, y) > 3:
                    grid[x][y] = 0
            elif countn(save, x, y) == 3:
                grid[x][y] = 1             
    return grid
            
def countn(grid, x, y):
    if x == 0 or y == 0 or x == res - 1 or y == res - 1:
        return 1
    else:
        return grid[x][y-1] + grid[x][y+1] + grid[x+1][y]+ grid[x+1][y-1] + grid[x+1][y+1] + grid[x-1][y] + grid[x-1][y+1] + grid[x+1][y-1]
    





for x in range(res):
    grid.append([])
    for y in range(res):
        grid[x].append(random.randint(0, 1))

        
for x in range(res):
    for y in range(res):
        pygame.draw.rect(screen, (0, 255*grid[x][y], 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))

pygame.display.flip()
running = True


while running:
    update(grid)
    for x in range(res):
        for y in range(res):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
            else:
                pygame.draw.rect(screen, (0, 255, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        running = False
    dt = clock.tick(5) / 1000
    
    pygame.display.flip()
    
pygame.quit()
