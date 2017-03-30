#!~usr/bin/env python3

import screen
import draw
import matrix
import random
import time

def parseFile(fileName, screens, color, edgeMatrix, transformMatrix):
    scriptFile = open('{}'.format(fileName), 'r')
    for line in scriptFile:
        currentLine = line.split()
        if(currentLine[0][0] == '#'):
            pass
        elif(currentLine[0] == 'line'):
            argumentLine = scriptFile.readline().split()
            a = [ float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]) ]
            b = [ float(argumentLine[3]), float(argumentLine[4]), float(argumentLine[5]) ]
            matrix.addEdge(edgeMatrix, a, b)
        elif(currentLine[0] == 'ident'):
            matrix.setIdentityMatrix(transformMatrix)
        elif(currentLine[0] == 'move'):
            argumentLine = scriptFile.readline().split()
            moveMatrix = matrix.createTranslateMatrix( float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]))
            matrix.matrixMultiplication(moveMatrix, transformMatrix)
        elif(currentLine[0] == 'scale'):
            argumentLine = scriptFile.readline().split()
            scaleMatrix = matrix.createScaleMatrix( float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]) )
            matrix.matrixMultiplication(scaleMatrix, transformMatrix)
        elif(currentLine[0] == 'rotate'):
            argumentLine = scriptFile.readline().split()
            rotateMatrix = matrix.createRotateMatrix(argumentLine[0], float(argumentLine[1]))
            matrix.matrixMultiplication(rotateMatrix, transformMatrix)
        elif(currentLine[0] == 'circle'):
            argumentLine = scriptFile.readline().split()
            draw.circle(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), 0 )
        elif(currentLine[0] == 'hermite'):
            argumentLine = scriptFile.readline().split()
            draw.curve(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), float(argumentLine[4]), float(argumentLine[5]), float(argumentLine[6]), float(argumentLine[7]), 0, 'hermite')
        elif(currentLine[0] == 'bezier'):
            argumentLine = scriptFile.readline().split()
            draw.curve(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), float(argumentLine[4]), float(argumentLine[5]), float(argumentLine[6]), float(argumentLine[7]), 0, 'bezier')
        elif(currentLine[0] == 'box'):
            argumentLine = scriptFile.readline().split()
            draw.box(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), float(argumentLine[4]), float(argumentLine[5]) )
        elif(currentLine[0] == 'sphere'):
            argumentLine = scriptFile.readline().split()
            draw.sphere(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), 0)
        elif(currentLine[0] == 'torus'):
            argumentLine = scriptFile.readline().split()
            draw.torus(edgeMatrix, float(argumentLine[0]), float(argumentLine[1]), float(argumentLine[2]), float(argumentLine[3]), float(argumentLine[4]), 0 )
        elif(currentLine[0] == 'clear'):
            edgeMatrix = [ [], [], [], [] ]
        elif(currentLine[0] == 'apply'):
            matrix.matrixMultiplication(transformMatrix, edgeMatrix)
        elif(currentLine[0] == 'display'):
            matrix.drawEdges(screens, edgeMatrix, color)
            screen.display(screens)
            screen.clearScreen(screens)
            time.sleep(.01)
        elif(currentLine[0] == 'save'):
            argumentLine = scriptFile.readline().split()
            matrix.drawEdges(screens, edgeMatrix, color)
            screen.saveExtension(screens, argumentLine[0])
        else:
            print('Bad command, ' + currentLine[0])
