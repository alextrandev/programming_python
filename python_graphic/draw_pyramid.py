"""
File: draw_pyramid.py
---------------------------
Draw a perfect pyramid with pre-defined brick size. Each higer row have 1 less brick and the pyramid should be centered on the canvas
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # this loop will draw rows based on number of brick at the bottom row
    for i in range (BRICKS_IN_BASE):
        draw_brick_row(canvas, 14 - i, i + 1)
    
def draw_brick_row(canvas, n, row):
    ROW_START_X = (CANVAS_WIDTH - n * BRICK_WIDTH) / 2
    ROW_START_Y = CANVAS_HEIGHT - row * BRICK_HEIGHT # the row start position is based on nubmer of brick on that row
    # this loop will draw a row of brick based on number of brick passed as "n", the row parameter is the position of the row
    for i in range(n):
        draw_brick(
            canvas,
            ROW_START_X + i * BRICK_WIDTH,
            ROW_START_Y
        )

def draw_brick(canvas, x, y): # A simple draw brick function take the start coordinates and draw a given sized brick
    canvas.create_rectangle(
    x, y, 
    x + BRICK_WIDTH, y + BRICK_HEIGHT, 
    "yellow", "black"
)
    

if __name__ == '__main__':
    main()