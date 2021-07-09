""" -- Food Sprite File --

Class: Food_Sprite()

Functions:  __init__()
            update()
"""
from data import constants
import arcade



class FoodSprite(arcade.Sprite):
    """ This class creates the movement of the food sprites and plays a sound on collision.
    
    Stereotype:
        Information Holder

    Attributes:
        size (integer): holds the size of each food sprite.
        type_of_food (string): holds the type of food (good or bad).
    """

    def __init__(self, image_file_name, SCALE, good_bad = 'bad'):
        """The class constructor.
        
        Args:
            self (FoodSprite): an instance of FoodSprite.
            image_file_name (Constants): holds the image file for each instance of food sprites.
            good_bad (string): holds value of type_of_food.
        """        
        super().__init__(image_file_name, constants.SCALE)
        self.size = 0
        self.type_of_food = good_bad
        if self.type_of_food == 'bad':
            self.eating_sound = constants.assets_dir + "/sounds/laser1.ogg"
        elif self.type_of_food == 'good':
            self.eating_sound = constants.assets_dir + "/sounds/laser1.ogg"

    def update(self):
        """ Moves the food around in different directions.
        
        Args:
            self (FoodSprite): an instance of FoodSprite.
        """  
        super().update()
        if self.center_x < constants.LEFT_LIMIT:
            self.center_x = constants.RIGHT_LIMIT
        if self.center_x > constants.RIGHT_LIMIT:
            self.center_x = constants.LEFT_LIMIT
        if self.center_y > constants.TOP_LIMIT:
            self.center_y = constants.BOTTOM_LIMIT
        if self.center_y < constants.BOTTOM_LIMIT:
            self.center_y = constants.TOP_LIMIT
