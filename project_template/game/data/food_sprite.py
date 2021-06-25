from data import constants
import arcade

class FoodSprite(arcade.Sprite):
    """ Sprite that represents an food. """

    def __init__(self, image_file_name, SCALE, good_bad = 'bad'):
        super().__init__(image_file_name, constants.SCALE)
        self.size = 0
        self.type_of_food = good_bad
        if self.type_of_food == 'bad':
            self.eating_sound = "../assets/sounds/laser1.ogg"
        elif self.type_of_food == 'good':
            self.eating_sound = "../assets/sounds/laser1.ogg"

    def update(self):
        """ Move the food around. """
        super().update()
        if self.center_x < constants.LEFT_LIMIT:
            self.center_x = constants.RIGHT_LIMIT
        if self.center_x > constants.RIGHT_LIMIT:
            self.center_x = constants.LEFT_LIMIT
        if self.center_y > constants.TOP_LIMIT:
            self.center_y = constants.BOTTOM_LIMIT
        if self.center_y < constants.BOTTOM_LIMIT:
            self.center_y = constants.TOP_LIMIT
