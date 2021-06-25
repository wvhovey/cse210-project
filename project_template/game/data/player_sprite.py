from data import constants
import arcade
import math

class PlayerSprite(arcade.Sprite):
    """
    Sprite that represents our player.

    Derives from arcade.Sprite.
    """
    def __init__(self, filename, SCALE):
        """ Set up the player. """

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
        """
        Called when we die and need to make a new player.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = True
        self.center_x = constants.SCREEN_WIDTH / 2
        self.center_y = constants.SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        """ Move the player """
        # Move player.

        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        # if self.speed > 0:
        #     self.speed -= self.drag
        #     if self.speed < 0:
        #         self.speed = 0

        # if self.speed < 0:
        #     self.speed += self.drag
        #     if self.speed > 0:
        #         self.speed = 0

        # if self.speed > self.max_speed:
        #     self.speed = self.max_speed
        # if self.speed < -self.max_speed:
        #     self.speed = -self.max_speed

        # self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        # self.change_y = math.cos(math.radians(self.angle)) * self.speed

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