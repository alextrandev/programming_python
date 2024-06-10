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
    for i in range (14):
        draw_brick_row(canvas, 14 - i, i + 1)
    
def draw_brick_row(canvas, n, row):
    ROW_START_X = (CANVAS_WIDTH - n * BRICK_WIDTH) / 2
    ROW_START_Y = CANVAS_HEIGHT - row * BRICK_HEIGHT
    for i in range(n):
        draw_brick(
            canvas,
            ROW_START_X + i * BRICK_WIDTH,
            ROW_START_Y
        )

def draw_brick(canvas, x, y):
    canvas.create_rectangle(
    x, y, 
    x + BRICK_WIDTH, y + BRICK_HEIGHT, 
    "yellow", "black"
)
    

if __name__ == '__main__':
    main()