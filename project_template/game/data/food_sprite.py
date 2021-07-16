""" -- food sprite file --

class: food_sprite()

functions:  __init__()
            update()
"""
from data import constants
import arcade



class foodsprite(arcade.Sprite):
    """ this class creates the movement of the food sprites and plays a sound on collision.
    
    stereotype:
        information holder

    attributes:
        size (integer): holds the size of each food sprite.
        type_of_food (string): holds the type of food (good or bad).
    """

    def __init__(self, image_file_name, scale, width, height, good_bad = 'bad'):
        """the class constructor.
        
        args:
            self (foodsprite): an instance of foodsprite.
            image_file_name (constants): holds the image file for each instance of food sprites.
            good_bad (string): holds value of type_of_food.
        """        
        super().__init__(image_file_name, constants.scale)
        self.size = 0
        self.type_of_food = good_bad
        if self.type_of_food == 'bad':
            self.eating_sound = constants.assets_dir / "sounds" / "laser1.ogg"
        elif self.type_of_food == 'good':
            self.eating_sound = constants.assets_dir / "sounds" / "laser1.ogg"
        self.screen_width = width
        self.screen_height = height

    def update(self):
        """ moves the food around in different directions.
        
        args:
            self (foodsprite): an instance of foodsprite.
        """  
        super().update()
        if self.center_x < constants.left_limit:
            self.center_x = self.screen_width + constants.offscreen_space
        if self.center_x > self.screen_width + constants.offscreen_space:
            self.center_x = constants.left_limit
        if self.center_y > self.screen_height + constants.offscreen_space:
            self.center_y = constants.bottom_limit
        if self.center_y < constants.bottom_limit:
            self.center_y = self.screen_height + constants.offscreen_space
