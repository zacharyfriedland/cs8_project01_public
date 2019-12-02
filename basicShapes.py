#basicShapes.py, Zachary Friedland
import turtle

def drawRectangle1(t):
    """
    Draw a rectangle with width 50 and height 100. Use a turtle called t to create the drawing
    Note that the parameter is called t; t stands in place of whatever turtle was passed in.
    """
    t.color("green", "yellow") #makes pen green and fill yellow
    t.seth(0)   # Set the initial orientation of the turtle to 0 degrees
    t.begin_fill()#start filling
    t.forward(50)   # Move the turtle forward by 50 units in the direction that it was pointing
    t.left(90)  # Turn the turtle left by 90 degrees relative to the direction it was pointing
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90) #put turtle in initial orientation
    t.end_fill()


def drawRectangle(t, width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. After the rectangle is drawn, the turtle should return to its original position with an orientation of 0 degrees with respect to the x-axis.
    Use a turtle called t to create the drawing
    """
    t.color(penColor, fillColor)
    t.seth(tilt)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def drawTwoRectangles(t):
    drawRectangle(t, 50, 100, 0, "red", "") 
    t.seth(0)   
    t.up()     
    t.forward(100)  
    t.down()

    drawRectangle(t, 100, 150, 22, "green", "yellow") 

def drawTriangle(t, side, penColor, fillColor):
    t.color(penColor, fillColor)
    t.seth(0)
    t.begin_fill()
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.seth(0)
    t.end_fill()

def drawTwoTriangles(t):
    drawTriangle(frank, 50, "purple", "yellow")
    t.up()
    t.forward(20)
    t.down()
    drawTriangle(t, 80, "orange", "black")

if __name__=="__main__":
    frank = turtle.Turtle()
    frank.shape("turtle")
    frank.speed(.7)
    frank.width(4)
    #drawRectangle1(frank)
    #drawRectangle(frank, 40, 75, 45, "blue", "yellow")
    drawTwoRectangles(frank)
    frank.up()
    frank.forward(120)
    frank.down()
    #drawTriangle(frank, 50, "green", "blue")
    drawTwoTriangles(frank)
