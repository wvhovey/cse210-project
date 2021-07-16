""" -- instruction menu file --

class: instruction_menu()

functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import random
import arcade
from arcade.gui import UIManager
from data import constants

class instruction_menu(arcade.View):
    """ this class creates the instruction menu when the player pushes a specified button.
    
    stereotype:
        information holder

    attributes:
        instruction_view (object): holds the information for the instruction view.

    """

    def __init__(self, pause_view):
        """ the class constructor.
        
        args:
            self (instruction_menu): an instance of instruction_menu.
            pause_view (object): an instance of pause_view.
        """   
        super().__init__()
        self.instruction_view = pause_view

    def on_show(self):
        """ sets the background color of the instruction menu.
        
        args:
            self (instruction_menu): an instance of instruction_menu.
        """   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ creates the view for the instruction menu.
        
        args:
            self (instruction_menu): an instance of instruction_menu.
        """  
        arcade.start_render()

        arcade.draw_text("instructions", self.window.width/2, self.window.height/2+140,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("press esc. to return",
                         self.window.width/2,
                         self.window.height/2+90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("the goal of the game is to not die from being obese or underweight",
                         self.window.width/2,
                         self.window.height/2+30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("to win, you must live for 1 minute. watch the timer on the bottom left!",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("press w to move up, s to move down",
                         self.window.width/2,
                         self.window.height/2-60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("press a to move left, d to move right",
                         self.window.width/2,
                         self.window.height/2-90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("gather unhealthy foods to increase your weight",
                         self.window.width/2,
                         self.window.height/2-120,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("gather healthy foods to decrease your weight",
                         self.window.width/2,
                         self.window.height/2-150,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("don't go below 100 weight or above 400 weight or you will lose",
                         self.window.width/2,
                         self.window.height/2-180,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        """ allows the user to resume the game on key press.
        
        args:
            self (instruction_menu): an instance of instruction_menu.
            key (arcade.key): sets esc key to resume the game.
        """ 
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.instruction_view)