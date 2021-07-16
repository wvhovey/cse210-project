""" -- pause menu file --

class: pause_menu()

functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import random
import arcade
from data import constants
from arcade.gui import UIManager
from data.instruction_menu import instruction_menu

class pause_menu(arcade.View):
    """ this class creates the pause menu when when the player pushes a specified button.
    
    stereotype:
        information holder

    attributes:
        game_view (object): holds the information for the current game view.
        ui_manager(UIManager): manages the ui and the pause menu buttons.

    """
    def __init__(self, game_view):
        """ the class constructor.
        
        args:
            self (pause_menu): an instance of pause_menu.
            game_view (object): an instance of game_view.
        """   
        super().__init__()
        self.game_view = game_view
        self.ui_manager = UIManager()

    def on_show(self):
        """ sets the background color of the pause menu.
        
        args:
            self (pause_menu): an instance of pause_menu.
        """   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ creates the view for the pause menu.
        
        args:
            self (pause_menu): an instance of pause_menu.
        """  
        arcade.start_render()

        # draw player, for effect, on pause screen.
        # the previous view (gameview) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.BLACK + (200,))

        arcade.draw_text("paused", self.window.width/2, self.window.height/2+50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        # show tip to return or reset
        arcade.draw_text("press esc. to return",
                         self.window.width/2,
                         self.window.height/2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("press enter to view instructions",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ allows the user to resume the game on key press.
        
        args:
            self (pause_menu): an instance of pause_menu.
            key (arcade.key): sets esc key to resume the game.
        """ 
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # instruction menu
            instruction = instruction_menu(self)
            self.window.show_view(instruction)