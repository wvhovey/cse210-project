""" -- Instruction Menu File --

Class: Instruction_Menu()

Functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import random
import arcade
from arcade.gui import UIManager
from data import constants

class Instruction_Menu(arcade.View):
    """ This class creates the Instruction menu when the player pushes a specified button.
    
    Stereotype:
        Information Holder

    Attributes:
        instruction_view (object): holds the information for the instruction view.

    """

    def __init__(self, pause_view):
        """ The class constructor.
        
        Args:
            self (Instruction_Menu): an instance of Instruction_Menu.
            pause_view (object): an instance of pause_view.
        """   
        super().__init__()
        self.instruction_view = pause_view

    def on_show(self):
        """ Sets the background color of the instruction menu.
        
        Args:
            self (Instruction_Menu): an instance of Instruction_Menu.
        """   
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Creates the view for the instruction menu.
        
        Args:
            self (Instruction_Menu): an instance of Instruction_Menu.
        """  
        arcade.start_render()

        arcade.draw_text("INSTRUCTIONS", self.window.width/2, self.window.height/2+140,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press Esc. to return",
                         self.window.width/2,
                         self.window.height/2+90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("The goal of the game is to not die from being obese or underweight",
                         self.window.width/2,
                         self.window.height/2+30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("To win, you must live for 1 minute. Watch the timer on the bottom left!",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press W to move up, S to move down",
                         self.window.width/2,
                         self.window.height/2-60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press A to move left, D to move right",
                         self.window.width/2,
                         self.window.height/2-90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Gather unhealthy foods to increase your weight",
                         self.window.width/2,
                         self.window.height/2-120,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Gather healthy foods to decrease your weight",
                         self.window.width/2,
                         self.window.height/2-150,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Don't go below 100 weight or above 400 weight or you will lose",
                         self.window.width/2,
                         self.window.height/2-180,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        """ Allows the user to resume the game on key press.
        
        Args:
            self (Instruction_Menu): an instance of Instruction_Menu.
            key (arcade.key): sets esc key to resume the game.
        """ 
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.instruction_view)