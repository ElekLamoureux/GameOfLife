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
def draw(grid, res):
    for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                    x, y = pygame.mouse.get_pos()
                    print(f"Mouse clicked at: ({x}, {y})")
                    grid[int(x/pixilsize)][int(y/pixilsize)] = 1 - grid[int(x/pixilsize)][int(y/pixilsize)]
                    
                    

#make grid
grid = []
for x in range(res):
    grid.append([])
    for y in range(res):
        grid[x].append(random.randint(0, 1))
        #grid[x].append(0)

#grid[1][2] = 1
#grid[2][3] = 1
#grid[3][1] = 1
#grid[3][2] = 1
#grid[3][3] = 1
        
running = True
r = random.randint(0, 255)
g = random.randint(100, 255)
b = random.randint(0, 255)
while running:
    #seems to be in every pygame loop? Allows for stopping of program? Still dont fully understand
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw new rectangles            
    for x in range(res):
        for y in range(res):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (r, g, b), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x*pixilsize, y*pixilsize, pixilsize, pixilsize))
    #update the grid            
    update(grid)
    #keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        running = False
    if keys[pygame.K_SPACE]:
        print("spacebar was pressed!")
        go = True
        pygame.time.wait(100)
        #while go:            
        #    pygame.time.wait(1)
        #    keys = pygame.key.get_pressed()
        #    if keys[pygame.K_SPACE]:
        #        go = False
        while go:
                pygame.time.wait(1)
                for event in pygame.event.get():  # Check new events inside the loop
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        go = False
                        pygame.time.wait(200)
    draw(grid,res)
    
            
    
    
    dt = clock.tick(100) / 1000
    
    pygame.display.flip()
    
pygame.quit()
