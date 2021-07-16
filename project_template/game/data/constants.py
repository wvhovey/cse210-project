""" -- constants file --

declares constant variables globally
for all files within this program

"""
from pathlib import Path
root = Path(__file__).parent.resolve()
assets_dir = root / "assets"  
# print(assets_dir)
starting_food_count = 10
scale = 0.5
offscreen_space = 10
screen_width = 800
screen_height = 600
screen_title = "food smasher"
left_limit = -offscreen_space
right_limit = screen_width + offscreen_space
bottom_limit = -offscreen_space
top_limit = screen_height + offscreen_space
movement_speed = 5