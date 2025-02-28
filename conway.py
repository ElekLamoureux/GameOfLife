# Example file showing a circle moving on screen
import pygame
import random
# pygame setup
pygame.init()
width = 1000
height = 1000
res = 100
pixilsize = width / res
screen = pygame.display.set_mode((width, height))
screen.fill("white")

pygame.draw.rect(screen, (0, 200, 0), (500, 500, 100, 200))
grid = []
for x in range(res):
    grid.append([])
    for y in range(res):
        grid[x].append([pixilsize * x, pixilsize*y])
        col = random.randint(0, 2)
        if col == 0:            
            pygame.draw.rect(screen, (0, 0, 0), (grid[x][y][0], grid[x][y][1], pixilsize, pixilsize))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (grid[x][y][0], grid[x][y][1], pixilsize, pixilsize))

#    pygame.draw.rect(screen, (0, 200, 0), (random.randint(0, 1000), random.randint(0, 1000), 100, 200))
print(grid)
pygame.display.flip()
#running = True
#while running:
#    pygame.display.flip()
#    pygame.draw.circle(screen, "red", (0, 0), 40)
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_x]:
#        running = false
#pygame.quit()
