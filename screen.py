#!~/usr/bin/env python3

from subprocess import Popen, PIPE
from os import remove
import screen

# createScreen(width, height)
# Creates a 2D array representing pixels to later write as a ppm file.
## arguments:
## width: int; width of screen.
## height: int; height of screen.
def createScreen(width, height):
    
    screen = []
    
    for i in range(0, width):
        screen.append([])
        for j in range(0, height):
            screen[i].append([0,0,0])
            
    return screen
# All functions conform to drawing and accessing where:
# x increases from left to right,
# y increases from top to bottom.
#   0  1  2  3  4  5  6  7  8  9     #Rows: 1st element of 2D array.
# 0[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 1[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 2[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 3[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 4[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 5[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 6[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 7[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 8[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# 9[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# This example matrix would be representative of each pixel of the image to be written.


# clearScreen(screen)
# Sets all 'pixels' to black.
## arguments:
## screen: list of lists; the screen to be cleared.
def clearScreen(screen):
    
    for i in range(0, len(screen) ):
        for j in range(0, len(screen[i]) ):
            screen[i][j] = [0,0,0]

            
# writePpmFile(screen, fileName, #<1>#comment)
# Writes the data from a screen to a ppm file.
## arguments:
## screen: list of lists; the screen to be written.
## fileName: string; fileName of the screen.
def writePpmFile(screen, fileName):
    file = open('{}'.format(fileName), 'w')
    # creates new file with fileName and open it to edit/
    
    file.write('P3\n')
    # This line specifies the file format for the ppm image file.
    # for more info on ppm file formats:
    # https://en.wikipedia.org/wiki/Netpbm_format#File_format_description

    width = len(screen)
    height = len(screen[0])
    file.write('{} {} 255\n'.format( width, height ) )
    # This line specifies the width, height, and color depth of the ppm image file.
    
    #<1># If ever you wish to include a comment with the file:
    #<1># file.write('#{}\n'.format(comment))

    # width is nested in height because ppm writes an image a row at a time.
    # Column index is incremented within to achieve this.
    for i in range(0, height):
        for j in range(0, width):
            file.write('{} {} {}  '.format( screen[j][i][0], screen[j][i][1], screen[j][i][2] ) )
            # 2 spaces after a pixel to make each pixel stand out when viewed as text.
            
    file.close()
    # Close file for safety.

def saveExtension( screens, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    writePpmFile( screens, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screens ):
    ppm_name = 'pic.ppm'
    writePpmFile( screens, ppm_name )
    p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)
