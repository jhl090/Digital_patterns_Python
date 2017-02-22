# At the top of every file, always include the following information
# Author(s) name:
# SPIS login(s):
# Assignment: Week 2 Recursion and Induction
# Date: August 25, 2014
# 
# Description: Recursive methods for doing various things

from PIL import Image, ImageDraw
import math

def recProduct( a, b ):
    if b == 0:
        return 0
    else:
        return recProduct( a, b-1 )

# Use this as a template for your recursive drawing functions
# Copy and paste it.  Change the name, and change the
# drawing function that it calls to be the one that you write
# to draw the tree or the snowflake.
def firstDraw():
    # These first two lines will always be more or less the same
    # Though you're welcome to change the size of your image
    # (the second argument to new (200, 200)) and the background
    # color (the 3rd argument to new (0, 0, 0)).
    image = Image.new('RGB', (200,200), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # This line will change depending on what you are trying to draw
    drawPicture( draw )

    # This line will stay the same so that you can see what was drawn
    image.show()

# In your lab you will write different functions to draw different shapes
# The function below is just to familiarize you with PIL.
# Your functions will use recursion.
def drawPicture( draw ):
    ''' Draw a simple picture using a PIL ImageDraw object (draw) '''
    # Notice how below we are using 4 variables to keep track of the
    # starting and ending coordinates of the square.  We change
    # the values of the variables in order to draw each side, but keep
    # the function call exactly the same.  This template might help you
    # as you start thinking about drawing recursively.
    
    # draw the left vertical line in a square
    startx = 0
    starty = 200
    endx = 100 
    endy = 0
    draw.line( (startx, starty, endx, endy), fill="white", width=2)
    
    # draw the bottom line
    startx = 0
    starty = 200
    endx = 200
    endy = 200
    # endy is still 100, and startx is still 0
    draw.line( (startx, starty, endx, endy), fill="white", width=2)

    # draw the right side
    startx = 100
    starty = 0
    endx = 200
    endy = 200
    draw.line( (startx, starty, endx, endy), fill="white", width=2)

    # draw the top
    startx = 0
    starty = 0
    endx = 0
    endy = 0
    draw.line( (startx, starty, endx, endy), fill="white", width=2)
    
def firstSpiral():
	image = Image.new('RGB', (200,200), (0,0,0))
	draw = ImageDraw.Draw(image)
	spiral(initialLength, angle, multiplier,draw, startx, starty)
	image.show()

def spiral(initialLength, angle, multiplier,dr,startx,starty):
	if initialLength >1:
		endx= startx+initialLength*math.cos(angle)
		endy= starty+initialLength*math.sin(angle)
		dr.line((startx,starty,endx,endy))
		spiral(initialLength*multiplier, angle+math.pi/4, multiplier,dr, endx, endy)
		
			




trunkLength=100
height=7
startx1=200
starty1=400
angle1=math.pi/2*3
angle2=angle1

def drawTree():
    image = Image.new('RGB', (400,400), (0,0,0))
    draw = ImageDraw.Draw(image)
    tree(trunkLength, height,draw,angle1, angle2, startx1, starty1)
    image.show()


def tree(trunkLength, height,dr,angle1, angle2, startx1, starty1):
    if height>1:
        endx1=startx1+trunkLength*math.cos(angle1)
        endy1=starty1+trunkLength*math.sin(angle1)
        endx2=startx1+trunkLength*math.cos(angle2)
        endy2=starty1+trunkLength*math.sin(angle2)
        dr.line((startx1, starty1,endx1,endy1))
        dr.line((startx1, starty1,endx2,endy2))
        tree(trunkLength/2, height-1,dr,angle1+math.pi/4, angle1-math.pi/4, endx1, endy1)
        tree(trunkLength/2, height-1,dr,angle2+math.pi/4, angle2-math.pi/4, endx2, endy2)
        

sidelength = 100
levels=4
startx=66
starty=134
angle=0


def drawSnowflake():
    image=Image.new('RGB', (400,400), (0,0,0))
    draw = ImageDraw.Draw(image)
    snowflakeSide(sidelength, levels, draw, startx, starty,angle)
    image.show()

def snowflakeSide(sidelength, levels, dr, startx, starty,angle):
    if levels>0:
        endx=startx+sidelength*math.cos(angle)
        endy=starty+sidelength*math.sin(angle)
        dr.line((startx,starty,endx,endy))
        smallerTriangles(dr,levels, angle, startx, starty)
        snowflakeSide(sidelength, levels-1, dr, endx, endy, angle-math.pi/3*2)

def smallerTriangles(dr,levels, angle, startx, starty):
    if levels>0:
        endx=startx-sidelength/3*math.cos(angle)
        endy=starty-sidelength/3*math.sin(angle)
        dr.line((startx, starty, endx, endy))
        smallerTriangles(dr, levels-1, angle-math.pi/3*2, endx, endy)