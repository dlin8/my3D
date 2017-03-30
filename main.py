#!~/usr/bin/env python3

# to do list:
# parser issues
# comment matrix
# possible issues with transform
# comment new screen

import screen
import draw
import matrix
import parser

green = [0, 255, 0]
edgeMatrix = [ [],[],[],[] ]
tempScreen = screen.createScreen(4,4)
transformMatrix = matrix.getIdentityMatrix(tempScreen)[:]

def main():
    #screenOne = screen.createScreen(500,500)
    #draw.circle(edgeMatrix, 250, 250, 0, 50, .00001)
    #matrix.drawEdges(screenOne, edgeMatrix, green)
    
    # screen.display(screenOne)
    screenOne = screen.createScreen(500, 500)
    parser.parseFile('script3', screenOne, green, edgeMatrix, transformMatrix)
    matrix.drawEdges(screenOne, edgeMatrix, green)
    screen.display(screenOne)
    # screen.writePpmFile(screenOne, 'pic.ppm')

main()

    
# def theyDontChange(x):
#     x = x + 2
# def theyDontChange(x):
#     x[0] = 999
# x = [1, 2, 3]
# theyDontChange(x)
# print(x)
