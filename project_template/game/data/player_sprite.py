""" -- Player Sprite File --

Class: Player_Sprite()

Functions:  __init__()
            respawn()
            update()
            setup()
"""

from data import constants
import arcade
import math

class PlayerSprite(arcade.Sprite):

    """ This class is in charge of the user's character. Its appearance, movement, behavior,
        and respawn on collision.

    Stereotype: 
        Service Provider

    Attributes:
        speed (integer): Holds the speed of character's movement.
        max_speed (integer): sets the maximum speed the character can move.
        drag (integer): holds the drag on the character's movement.
        respawning (boolean): determines whether or not to respawn the character.
    """
    def __init__(self, filename, SCALE):
        """The class constructor.
        
        Args:
            self (PlayerSprite): An instance of PlayerSprite.
            filename (string): holds the filename of the character sprite.
            SCALE (Constants): holds the scale of the character.
        """

        # Call the parent Sprite constructor
        super().__init__(filename, SCALE)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.speed = 0
        self.max_speed = 4
        self.drag = 0 
        self.respawning = False

        # Mark that we are respawning.
        self.respawn()

    def respawn(self):

        """ This function is called when a collision takes place. This changes the appearance of 
            the player and creates invisibility frames.
        
        Args:
            self (PlayerSprite): An instance of PlayerSprite.

        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = True
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):

        """ This function updates the position of the player based on key presses. 
            If the player goes off-screen, they are moved to the other side of 
            the window.
        
        Args:
            self (PlayerSprite): An instance of PlayerSprite.
        """
        # Move player.

        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the player goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = constants.SCREEN_WIDTH

        if self.left > constants.SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = constants.SCREEN_HEIGHT

        if self.top > constants.SCREEN_HEIGHT:
            self.bottom = 0

        """ Call the parent class. """
        super().update()