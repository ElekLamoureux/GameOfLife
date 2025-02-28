#ElekLamoureux
#1 is up 0 is down
import turtle
import random
import math
pen = turtle.Turtle()
pen.speed(0)

def triangle(upDown, x, y, size):
    pen.penup()
    if upDown == 1:
        pen.goto(x, y+size)
        pen.setheading(300)
    else:
        pen.goto(x, y-size)
        pen.setheading(120)
    pen.pendown()
    for i in range(3):     
        pen.forward(math.sqrt(3)*size)
        pen.right(120)

        
def triangles(x, y, s, depth):
    if depth != 0:
        circ = ((2*s)/3)
        triangle(0, x, y + circ, s/3)
        triangle(1, x, y - circ, s/3)
        triangle(1, x+((math.sqrt(3)*circ)/2), y+(circ/2), s/3)
        triangle(1, x-((math.sqrt(3)*circ)/2), y+(circ/2), s/3)
        triangle(0, x+((math.sqrt(3)*circ)/2), y-(circ/2), s/3)
        triangle(0, x-((math.sqrt(3)*circ)/2), y-(circ/2), s/3)
        depth = depth - 1
        triangles(x, y + circ, s/3, depth)
        triangles(x, y - circ, s/3, depth)
        triangles(x+((math.sqrt(3)*circ)/2), y+(circ/2), s/3, depth)
        triangles(x-((math.sqrt(3)*circ)/2), y+(circ/2), s/3, depth)
        triangles(x+((math.sqrt(3)*circ)/2), y-(circ/2), s/3, depth)
        triangles(x-((math.sqrt(3)*circ)/2), y-(circ/2), s/3, depth)
        
        

    
    
def snowflake(x, y, bigness, depth):
    currDepth = 1
    triangle(1, x, y, bigness)
    triangle(0, x, y, bigness)
    triangles(x, y, bigness, depth)
large = int(input("How large should it be?"))
depth = int(input("How deep should this go(thats what he said)"))
snowflake(0, 0, large, depth)
snowflake(0, 2*large, large, depth)
snowflake(0, -2*large, large, depth)
snowflake(2*large, 0, large, depth)
snowflake(-2*large, 0, large, depth)


