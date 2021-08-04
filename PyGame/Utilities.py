import math

class Rectangle:
    '''x and y denote the top left point of the rectangle'''
    def __init__(self, width, height, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
    
    def __str__(self):
        output = "Width: " + self.width +"\n"
        output = "Height: "+self.height+"\n"
        output = "Position: ("+self.x+", "+self.y+")"
        return output

class Circle:
    '''x and y denote the center of the circle'''
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x=x
        self.y=y

    def __str__(self):
        output = "Radius: " + self.radius +"\n"
        output = "Position: ("+self.x+", "+self.y+")"
        return output

def RectsIntersect(rectA, rectB):
    return rectA.x + rectA.width > rectB.x and rectA < rectB.x+rectB.width and rectA.y + rectA.height > rectB.y and rectA.y < rectB.y + rectB.height

def CirclesIntersect(circleA, circleB):
    x = circleA.x - circleB.x
    y = circleA.y - circleB.y
    radii = circleA.radius - circleB.radius
    return x * x + y * y <= math.pow(radii, 2)

def PointCircleIntersect(pointX, pointY, circle):
    x = pointX - circle.x
    y = pointY - circle.y
    return x * x + y * y <= math.pow(circle.radius, 2)

# https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
def RectCircleIntersect(circle, rect):
    pass

def PointInRectangle():
    pass