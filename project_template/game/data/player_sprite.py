""" -- player sprite file --

class: player_sprite()

functions:  __init__()
            respawn()
            update()
            setup()
"""

from data import constants
import arcade
import math

class playersprite(arcade.Sprite):

    """ this class is in charge of the user's character. its appearance, movement, behavior,
        and respawn on collision.

    stereotype: 
        service provider

    attributes:
        speed (integer): holds the speed of character's movement.
        max_speed (integer): sets the maximum speed the character can move.
        drag (integer): holds the drag on the character's movement.
        respawning (boolean): determines whether or not to respawn the character.
    """
    def __init__(self, filename, scale, width, height):
        """the class constructor.
        
        args:
            self (playersprite): an instance of playersprite.
            filename (string): holds the filename of the character sprite.
            scale (constants): holds the scale of the character.
        """

        # call the parent sprite constructor
        super().__init__(filename, scale)

        # info on where we are going.
        # angle comes in automatically from the parent class.
        self.speed = 0
        self.max_speed = 4
        self.drag = 0 
        self.respawning = False
        self.screen_width = width
        self.screen_height = height

        # mark that we are respawning.
        self.respawn()

    def respawn(self):

        """ this function is called when a collision takes place. this changes the appearance of 
            the player and creates invisibility frames.
        
        args:
            self (playersprite): an instance of playersprite.

        """
        # if we are in the middle of respawning, this is non-zero.
        self.respawning = True
        self.center_x = self.screen_width / 2
        self.center_y = self.screen_height / 2
        self.angle = 0

    def update(self):

        """ this function updates the position of the player based on key presses. 
            if the player goes off-screen, they are moved to the other side of 
            the window.
        
        args:
            self (playersprite): an instance of playersprite.
        """
        # move player.

        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255

        self.center_x += self.change_x
        self.center_y += self.change_y

        # if the player goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = self.screen_width

        if self.left > self.screen_width:
            self.right = 0

        if self.bottom < 0:
            self.top = self.screen_height

        if self.top > self.screen_height:
            self.bottom = 0

        """ call the parent class. """
        super().update()