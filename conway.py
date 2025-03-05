#imports
import sys
import pygame
import random
import copy

#setup
pygame.init()
size = 500
res = 50
pixilsize = size / res
screen = pygame.display.set_mode((size, size))
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
    
      

def drawgrid(grid):
    for x in range(res):
            for y in range(res):
                if grid[x][y] == 1:
                    pygame.draw.rect(screen, (r, g, b), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))

#make grid
grid = []
for x in range(res):
    grid.append([])
    for y in range(res):
        grid[x].append(random.randint(0, 1))
        #grid[x].append(0)
count = 0
speed = 100

running = True
r = random.randint(0, 255)
g = random.randint(100, 255)
b = random.randint(0, 255)
unpaused = True
pendown = False
while running:
    pygame.display.flip()
    count = count + 1
    #seems to be in every pygame loop? Allows for stopping of program? Still dont fully understand
    
    if count == speed:
        if unpaused:          
            #update the grid            
            update(grid)
    if count == speed:
        count = 0
    #keypresses
    drawgrid(grid)    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        running = False
        
    if keys[pygame.K_SPACE]:
        print("spacebar was pressed!")
        count = 0
        if unpaused:
            unpaused = False
        else:
            unpaused = True
        pygame.time.wait(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            pendown = True
            checker = copy.deepcopy(grid)
        if event.type == pygame.MOUSEBUTTONUP:
            pendown = False
    if pendown:
        x, y = pygame.mouse.get_pos()
        cellx = int(x/pixilsize)
        celly = int(y/pixilsize)
        if grid[cellx][celly] == checker[cellx][celly]:
            grid[cellx][celly] = 1-grid[cellx][celly]        
            #print(f"Mouse down at: ({x}, {y})")        
            #print(f'Maps to cell (x,y) = ({cellx}, {celly})')
            drawgrid(grid)
        

    
    dt = clock.tick(10000)
    
    
pygame.quit()
