#!~/usr/bin/env python3

import screen
import matrix
import math

# plot(screen, x, y, color)
# Plots a point on a screen.
## parameters:
## screen: list of lists; screen to plot point onto.
## x: int; x-coordinate of point.
## y: int; y-coordinate of point.
## color: list [R,G,B]; color of point.
def plot(screen, x, y, color):
    width = len(screen)
    height = len(screen[0])
    if(x >= width or x < 0 or y >= height or y < 0):
        x = x%len(screen)
        y = y%len(screen)
        #print('Out of bounds!')
        # return False
    screen[x][y] = color
    
# drawLine(screen, a, b, color)
# Draws a line on a screen
## paramaters:
## screen: list of lists; screen to plot point onto.
## a: list [x-coordinate, y-coordinate]; coordinates of one endpoint of line.
## b: list [x-coordinate, y-coordinate]; coordinates of other endpoint of line.
## color: list [R,G,B]; color of line
def drawLine(screen, a, b, color):
    # Picture of Octants:
    # \3##|##2/
    # #\##|##/#
    # ##\#|#/##
    # 4##\|/##1
    # ---------
    # 5##/|\##8
    # ##/#|#\##
    # #/##|##\#
    # /6##|##7\

    # Reminder that the origin is in the top left, and y increments top to bottom.
    # Any work with y-values should have this in mind.
    
    # Swap points a and b if a is to the right of b.
    # Only have to deal with octants 1, 2, 7, and 8 as a result where we start from the left and draw to the right.
    if(b[0] < a[0]):
        # Swapping values without a third variable.
        # Possibility for overflow errors.
        b[0] = b[0] + a[0]
        a[0] = b[0] - a[0]
        b[0] = b[0] - a[0]
        
        b[1] = b[1] + a[1]
        a[1] = b[1] - a[1]
        b[1] = b[1] - a[1]

    x = a[0]
    y = a[1]
    # Initialize x and y coordinates of current pixel to be drawn.

    # y = mx + b
    ## m = dy / dx
    # 0 = mx - y + b
    # multiply both sides by dx.
    # 0 = (dy * x) - (dx * y) + (dx * b)
    # 0 = Ax + By + C
    # A =  dy
    # B = -dx
    # C =  dx * b
    
    B = -1 * (b[0] - a[0])
    # (B = -dx) point b is always to the right of a because we swapped if not.
    # b[0] >= a[0]
    # B = -1 * (b[0] - a[0])
    
    # Algorithm follows this general structure:
    # One coordinate will always be incremented.
    # The other coordinate will either be or not be incremented.
    # This depends on the midpoint of these two possible spaces for the new pixel.
    # The midpoint is substituted into the standard form of the equation representing the line.
    # Depending on whether this value is positive or negative,
    # We can determine that most of the line resides in one or the other space.
    # And we can then decide to increment or not increment to have the next pixel be in that space.

    # Midpoint calculations:
    # f(X0 + i, Y0 + j) = A(X0+i) + B(Y0+j) + C
    # = AX0 + Ai + BY0 + Bj + C
    #                               AX0 + BY0 + C = 0
    # = Ai + Bj
    # i is 0.5 or 1, j is 1 or 0.5, representative of midpoint coordinates.
    # Multiply by 2 to avoid division.
    # Increment A and B twice as well to stay consistent with this scaled value of midpoint.
    
    if a[1] >= b[1]:
        # Octants 1, 2, horizontal line, or perfect diagonal SW - NE.
        # [0, pi/2)
        # If point a is LOWER than point b, see reminder text.
        # Also track if a and b are of same height for trivial case. (Hoz. line)
        
        A = a[1] - b[1]
        # A = dy
        
        if abs(A) >= abs(B):
            # If y increases faster than x, or increase at the same rate:
            # Line resides in octant 2 or between octants 1 and 2 for 45 deg line.
            # [pi/4, pi/2)
            
            # ##2/
            # ##/
            # #/
            # /
            # picture of an octant 2 line.

            # [?][?]
            # [X][_]
            # how next pixel is decided.

            # f(X+0.5, Y+0.1)
            # f(X+1, Y+2)
            # A + 2B
            
            d = A + (2 * B)
            # B is negative!
            # Initial value of midpoint.
            # A positive value indicates that A > 2B.
            # Therefore, the x-coordinate of the midpoint, the conditional coordinate is too high.
            # Therefore, if d is > 0, do not increment x.
            # Otherwise, if d is < 0, do increment x.
            # if d = 0 dont increment, stays consistent with other 3 quadrants.
            
            while(y >= b[1]):
                plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + (2*A)
                y = y - 1
                d = d + (2*B)
        else:
            # Otherwise, the line resides in octant 1.
            # [0, pi/4)

            # ####/
            # #___#
            # /###1
            # picture of octant 1 line

            # [_][?]
            # [X][?]
            # how next pixel is decided.

            # f(X+1, Y+0.5)
            # f(X+2, Y+1)
            # 2A + B

            # Here the conditional coordinate is Y. Reminder text.
            # B is the only negative term.
            # d > 0 means that Y is too low.
            d = (2 * A) + B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d > 0):
                    y = y - 1 #REMINDER TEXT
                    d = d + (2*B)
                x = x + 1
                d = d + (2*A)
    else:
        # Otherwise the point a is HIGHER than b.
        # Octant VII, VIII, edge cases.
        # (0, -pi/2]
        
        A = a[1] - b[1]
        #
        if abs(A) >= abs(B):
            # Y changes faster or equal to X, Octant 7 or perfect diagonal NW-SE.
            # [-pi/4, -pi/2]

            # [X][_]
            # [?][?]

            # f(X+0.5, Y-1)
            # f(X+1, Y-2)
            # d = A - 2B

            d = A - (2 * B)
            while(y <= b[1]):
                plot(screen, x, y, color)
                if(d > 0):
                    # X is not high enough
                    x = x + 1
                    d = d + (2*A) 
                y = y + 1
                    # Reminder text.
                d = d - (2*B)
                # Decrement because y is DECREASING, b term must decrease as well.
                # Confusing because b is actually negative, so d is actually increasing.
            
        else:
            # Octant 8.
            # (0, -pi/4)

            # [X][?]
            # [_][?]

            # f(X+1, Y-0.5)
            # f(X+2, Y-1)
            # d = 2A - B
            
            d = (2 * A) - B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d < 0):
                    # Y is too high.
                    y = y + 1
                    d = d - (2*B)
                x = x + 1
                d = d + (2*A)

def circle(edgeMatrix, x, y, z, r, step):
    # it doesn't get any finer, waste time otherwise.
    if step < (1 / (r * r)):
        step = (1 / (r * r))
    t = 0
    while t < 1:
        matrix.addEdge(edgeMatrix,
                       
                       [r*math.cos( 2*math.pi*t ) + x,
                        r*math.sin( 2*math.pi*t ) + y,
                        z,
                        1],
                       
                       [r * math.cos( 2*math.pi*(t+step) ) + x,
                        r * math.sin( 2*math.pi*(t+step) ) + y,
                        z,
                        1]
                       
                       )
        t = t + step

def curve(edgeMatrix, x0, y0, x1, y1, x2, y2, x3, y3, step, curveType):
    if step == 0:
        step = 1 / 100.0
    coefX = matrix.generateCoef( x0, x1, x2, x3, curveType )
    coefY = matrix.generateCoef( y0, y1, y2, y3, curveType )
    newX = x0
    newY = y0
    t = 0
    while t < 1:
        t = t + step
        oldX = newX
        oldY = newY
        newX = (coefX[0][0] * math.pow(t, 3)) + (coefX[1][0] * math.pow(t, 2)) + (coefX[2][0] * t) + coefX[3][0]
        newY = (coefY[0][0] * math.pow(t, 3)) + (coefY[1][0] * math.pow(t, 2)) + (coefY[2][0] * t) + coefY[3][0]
        
        matrix.addEdge( edgeMatrix, [oldX, oldY, 0], [newX, newY, 0] )

def box(edgeMatrix, x, y, z, w, h, d):
    matrix.addEdge( edgeMatrix, [x, y, z], [x, y, z] )
    matrix.addEdge( edgeMatrix, [x, y+h, z], [x, y+h, z] )
    matrix.addEdge( edgeMatrix, [x+w, y, z], [x+w, y, z] )
    matrix.addEdge( edgeMatrix, [x+w, y+h, z], [x+w, y+h, z] )
    matrix.addEdge( edgeMatrix, [x, y, z-d], [x, y, z-d] )
    matrix.addEdge( edgeMatrix, [x, y+h, z-d], [x, y+h, z-d] )
    matrix.addEdge( edgeMatrix, [x+w, y, z-d], [x+w, y, z-d] )
    matrix.addEdge( edgeMatrix, [x+w, y+h, z-d], [x+w, y+h, z-d] )

def semicircle(edgeMatrix, x, y, z, r, step):
    if step < (1 / (r * r)):
        step = (1 / (r * r))
    phi = 0
    
    while t < .5:
        matrix.addEdge(edgeMatrix,
                       
                       [r*math.cos( 2*math.pi*t ) + x,
                        r*math.sin( 2*math.pi*t ) + y,
                        z,
                        1],
                       
                       [r * math.cos( 2*math.pi*(t+step) ) + x,
                        r * math.sin( 2*math.pi*(t+step) ) + y,
                        z,
                        1]
                       
                       )
        t = t + step
        
def sphere(edgeMatrix, cx, cy, cz, r, step):
    if step == 0:
        step = .025
    phi = 0
    while phi < (2 * math.pi):
        rotate = [ [1, 0, 0, 0],
                   [0, math.cos(phi), math.sin(phi), 0],
                   [0, math.sin(phi), -1 * math.cos(phi) ,0],
                   [0, 0, 0, 1] ]
        theta = 0
        while theta < math.pi:
            semicircle = [ [r * math.cos(theta)],
                           [r * math.sin(theta)],
                           [0],
                           [1] ]
            matrix.matrixMultiplication( rotate, semicircle )
            matrix.addEdge( edgeMatrix,
                            [semicircle[0][0]+cx, semicircle[1][0]+cy, semicircle[2][0]+cz],
                            [semicircle[0][0]+cx, semicircle[1][0]+cy, semicircle[2][0]+cz] )
            theta = theta + (math.pi / 30)
        phi = phi + (step * 2 * math.pi)

def torus(edgeMatrix, cx, cy, cz, r, R, step):
    if step == 0:
        step = .025
    phi = 0
    while phi < (2 * math.pi):
        rotate = [ [math.cos(phi), 0, math.sin(phi), 0],
                   [0, 1, 0, 0],
                   [ -1 * math.sin(phi), 0, math.cos(phi) ,0],
                   [0, 0, 0, 1] ]
        theta = 0
        while theta < (2 * math.pi):
            circle = [ [ (r * math.cos(theta) ) + R],
                       [r * math.sin(theta)],
                       [0],
                       [1] ]
            matrix.matrixMultiplication( rotate, circle )
            matrix.addEdge( edgeMatrix,
                            [circle[0][0]+cx, circle[1][0]+cy, circle[2][0]+cz],
                            [circle[0][0]+cx, circle[1][0]+cy, circle[2][0]+cz] )
            theta = theta + (2 * math.pi / 30)
        phi = phi + (step * 2 * math.pi)
    


    
    
