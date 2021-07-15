""" -- Pause Menu File --

Class: Pause_Menu()

Functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import random
import arcade
from data import constants
from arcade.gui import UIManager
from data.instruction_menu import Instruction_Menu

class Pause_Menu(arcade.View):
    """ This class creates the Pause menu when when the player pushes a specified button.
    
    Stereotype:
        Information Holder

    Attributes:
        game_view (object): holds the information for the current game view.
        ui_manager(UIManager): manages the ui and the pause menu buttons.

    """
    def __init__(self, game_view):
        """ The class constructor.
        
        Args:
            self (Pause_Menu): an instance of Pause_Menu.
            game_view (object): an instance of game_view.
        """   
        super().__init__()
        self.game_view = game_view
        self.ui_manager = UIManager()

    def on_show(self):
        """ Sets the background color of the Pause menu.
        
        Args:
            self (Pause_Menu): an instance of Pause_Menu.
        """   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Creates the view for the Pause menu.
        
        Args:
            self (Pause_Menu): an instance of Pause_Menu.
        """  
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.BLACK + (200,))

        arcade.draw_text("PAUSED", self.window.width/2, self.window.height/2+50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         self.window.width/2,
                         self.window.height/2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to view instructions",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Allows the user to resume the game on key press.
        
        Args:
            self (Pause_Menu): an instance of Pause_Menu.
            key (arcade.key): sets esc key to resume the game.
        """ 
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # instruction menu
            instruction = Instruction_Menu(self)
            self.window.show_view(instruction)