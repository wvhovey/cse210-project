""" -- Constants File --

Declares constant variables globally
for all files within this program

"""
from pathlib import Path
root = Path(__file__).parent
assets_dir = str(root)  + "\\assets\\"  

STARTING_food_COUNT = 10
SCALE = 0.5
OFFSCREEN_SPACE = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Food Smasher"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE
MOVEMENT_SPEED = 5