# Author: Eduardo Maciel de Souza

from graphics import *
from math import *

## GLOBAL VARIABLES 
DISPLAY_WIDTH = 800     # Screen's width
DISPLAY_HEIGHT = 600    # Screen's height

    # This values can be changed to produce different trees
branches = 12           # Number of branches on the tree (more branches demand more time to draw the tree)
size = 150              # Size of the first branch
color = [65, 208, 208]  # Finals branches' color

    # This variable is responsible for setting the color change
color_shift = list(map(lambda num: num//branches, color)) 

# This method determines the coordinates of a branch and create a guide line
def stick(point_init, angle, size):
    angle = -(angle + 180)%360
    x_f = point_init.getX() + sin(radians(angle))*size
    y_f = point_init.getY() + cos(radians(angle))*size
    point_final = Point(x_f, y_f)

    stick = Line(point_init, point_final)
    return stick

# This recursive method is responsible to create a bifurcation in the branch, and call yourself for every new branch 
def fractal_tree(point_init, angle, this_color, size, this_branch, window):
    if this_branch == 0:
        return 0

        # This values can be changed to produce different trees
    l_angle_rate = 25                # Left inclination
    r_angle_rate = 25                # Right inclination
    size_rate = .7                   # Define the size of the subsequent branches in relation to the previous branch

    L_branch = stick(point_init, angle-l_angle_rate, size)
    R_branch = stick(point_init, angle+r_angle_rate, size)
    L_branch.setOutline(color_rgb(this_color[0], this_color[1], this_color[2]))
    R_branch.setOutline(color_rgb(this_color[0], this_color[1], this_color[2]))
    L_branch.draw(window)
    R_branch.draw(window)

    
    this_color = list(map(lambda tup: tup[0] + tup[1], zip(this_color, color_shift)))
    fractal_tree(L_branch.getP2(), angle-l_angle_rate, this_color, size*size_rate, this_branch-1, window)
    fractal_tree(R_branch.getP2(), angle+r_angle_rate, this_color, size*size_rate, this_branch-1, window)

# The main function generates the window and initiates the tree
def main():
    window = GraphWin("Fractal Tree", DISPLAY_WIDTH, DISPLAY_HEIGHT)

    point_origin = Point(400, 550)                                      # This values refer to the tree's base

    black = [0, 0, 0]
    fractal_tree(point_origin, 0, black, size, branches, window)    
    window.getMouse()                                                   # Wait for a mouse click to close the window
    window.close()

main()

