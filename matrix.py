#!/usr/bin/env python3

import screen
import draw
import math

# Prints a matrix somewhat nicely
def printMatrix(matrix):
    printString = ''
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range (0, len(matrix) ):
        for j in range (0, len(matrix[0]) ):
            printString = printString + str(matrix[i][j]) + ' '
        printString = printString + '\n'
    print(printString)

# Performs scalar multiplication on a matrix
def scalarMultiplication(scalar, matrix):
    for row in range(0, len(matrix) ):
        for column in range(0, len(matrix[0])):
            matrix[row][column] = scalar * matrix[row][column]

    
## Test if this works with matrices of other dimensions
# This function is specific to 4xN edge matrix multiplied BY a 4x4 matrix
# Multiplier, Multiplicand

# matrix2 = matrix1 * matrix2
# usually transformMatrix, edgeMatrix
# most recent transformMatix, masterMatrix
def matrixMultiplication(matrix1, matrix2):
    for i in range(0, len( matrix2[0] ) ):
        tmp = []
        for j in range(0,4):
            tmp.append(matrix2[j][i])
        for k in range(0,4):
            matrix2[k][i] = dotProduct(matrix1[k][:], tmp)
        tmp = []

# Helper function for matrix multiplication         
def dotProduct(list1, list2):
    dotProduct = 0
    if len(list1) != len(list2):
        print('lists of unequal lengths')
        return False
    for i in range(0, len(list1)):
        dotProduct = dotProduct + (list1[i] * list2[i])
    return dotProduct

# Returns identity matrix of a given matrix
def getIdentityMatrix(matrix):
    length = max(len(matrix), len(matrix[0]))
    retMatrix = []
    for r in range(0, length):
        retMatrix.append([])
        for c in range(0, length):
            if(r == c):
                retMatrix[r].append(1)
            else:
                retMatrix[r].append(0)
    return retMatrix

# For parser
def setIdentityMatrix(matrix):
    for i in range( len(matrix) ):
        for j in range( len(matrix[i]) ):
            if(i == j):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

# Adds a point to edgeMatrix
def addPoint(matrix, a):
    matrix[0].append(a[0])
    matrix[1].append(a[1])
    matrix[2].append(a[2])
    matrix[3].append(1)

# Adds an edge to edgeMatrix using addPoint
def addEdge(matrix, a, b):
    addPoint(matrix, a)
    addPoint(matrix, b)

# Draws all the edges of edgeMatrix to screen with color
# Typecasts all floats to rounded ints for drawLine function
# They remain floats in the edgeMatrix
def drawEdges(screen, edges, color):
    for i in range(0, len( edges[0] ) - 1, 2):
        draw.drawLine(screen,
                      [ int( round( edges[0][i] ) ),
                        int( round( edges[1][i] ) ) ],
                        [ int( round( edges[0][i+1] ) ),
                          int( round( edges[1][i+1] ) ) ],
                          color )
# a, b, and c being the amount that each coordinate is translated by.
def createTranslateMatrix(a, b, c):
    translateMatrix = []
    for i in range(0,4):
        translateMatrix.append([])
        for j in range(0,4):
            if(i == j):
                translateMatrix[i].append(1)
            else:
                translateMatrix[i].append(0)
    translateMatrix[0][3] = a
    translateMatrix[1][3] = b
    translateMatrix[2][3] = c
    return translateMatrix
    
# a, b, and c being the amount that each coordinate is scaled by.
# Scales with respect to origin
def createScaleMatrix(a, b, c):
    scaleMatrix = []
    for i in range(0,4):
        scaleMatrix.append([])
        for j in range(0,4):
            if(i == j):
                scaleMatrix[i].append(1)
            else:
                scaleMatrix[i].append(0)
    scaleMatrix[0][0] = a
    scaleMatrix[1][1] = b
    scaleMatrix[2][2] = c
    return scaleMatrix

def createRotateMatrix(axis, theta):
    theta = math.radians(theta)
    rotateMatrix = []
    for i in range(0,4):
        rotateMatrix.append([])
        for j in range(0,4):
            if(i == j):
                rotateMatrix[i].append(1)
            else:
                rotateMatrix[i].append(0)
    if(axis == '0' or axis == 'x'):
        # y = ycostheta - zsintheta
        rotateMatrix[1][1] = math.cos(theta)        #ycostheta
        rotateMatrix[1][2] = (-1 * math.sin(theta)) #-zsintheta
        # z = zcostheta + ysintheta
        rotateMatrix[2][2] = math.cos(theta)        #zcostheta
        rotateMatrix[2][1] = math.sin(theta)        #ysintheta
        
    elif(axis == '1' or axis == 'y'):
        # z = zcostheta - xsintheta
        rotateMatrix[2][2] = math.cos(theta)        #zcostheta
        rotateMatrix[2][0] = (-1 * math.sin(theta)) #-xsintheta
        # x = xcostheta + zsintheta
        rotateMatrix[0][0] = math.cos(theta)        #xcostheta
        rotateMatrix[0][2] = math.sin(theta)        #zsintheta
        
    elif(axis == '2' or axis == 'z'):
        # x = xcostheta - ysintheta
        rotateMatrix[0][0] = math.cos(theta)        #xcostheta
        rotateMatrix[0][1] = (-1 * math.sin(theta)) #-ysintheta
        # y = ycostheta + xsinthetat
        rotateMatrix[1][1] = math.cos(theta)        #ycostheta
        rotateMatrix[1][0] = math.sin(theta)        #xsintheta

    return rotateMatrix

def makeHermite():
    hermiteMatrix = getIdentityMatrix( screen.createScreen(4,4) )
    hermiteMatrix[0][0] = 2.0
    hermiteMatrix[0][1] = -2.0
    hermiteMatrix[0][2] = 1.0
    hermiteMatrix[0][3] = 1.0
    
    hermiteMatrix[1][0] = -3.0
    hermiteMatrix[1][1] = 3.0
    hermiteMatrix[1][2] = -2.0
    hermiteMatrix[1][3] = -1.0
    
    hermiteMatrix[2][0] = 0.0
    hermiteMatrix[2][1] = 0.0
    hermiteMatrix[2][2] = 1.0
    hermiteMatrix[2][3] = 0.0

    hermiteMatrix[3][0] = 1.0
    hermiteMatrix[3][1] = 0.0
    hermiteMatrix[3][2] = 0.0
    hermiteMatrix[3][3] = 0.0
    
    return hermiteMatrix

def makeBezier():
    bezierMatrix = getIdentityMatrix( screen.createScreen(4,4) )
    bezierMatrix[0][0] = -1.0
    bezierMatrix[0][1] = 3.0
    bezierMatrix[0][2] = -3.0
    bezierMatrix[0][3] = 1.0
    
    bezierMatrix[1][0] = 3.0
    bezierMatrix[1][1] = -6.0
    bezierMatrix[1][2] = 3.0
    bezierMatrix[1][3] = 0.0
    
    bezierMatrix[2][0] = -3.0
    bezierMatrix[2][1] = 3.0
    bezierMatrix[2][2] = 0.0
    bezierMatrix[2][3] = 0.0

    bezierMatrix[3][0] = 1.0
    bezierMatrix[3][1] = 0.0
    bezierMatrix[3][2] = 0.0
    bezierMatrix[3][3] = 0.0

    return bezierMatrix

def generateCoef(p1, p2, p3, p4, t):
    coefMatrix = [ [p1], [p2], [p3], [p4], ]
    if( t == 'hermite' ):
        matrixMultiplication(makeHermite(), coefMatrix)
    elif( t == 'bezier' ):
        matrixMultiplication(makeBezier(), coefMatrix)
    else:
        print('invalid curve type')
    return coefMatrix
            
