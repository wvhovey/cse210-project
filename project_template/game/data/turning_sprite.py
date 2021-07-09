""" -- Turning Sprite File --

Class: TurningSprite()

Functions: update()

"""

import math
import arcade

class TurningSprite(arcade.Sprite):
    """ Calls the sprite that sets the angle of the food to the direction it is traveling in..

    Stereotype: 
        Service Provider

    Attributes:
        angle (float)
    """
    def update(self):
        """ Moves the sprite in the proper direction.
        
        Args:
            self (TurningSprite): An instance of TurningSprite.
        """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))