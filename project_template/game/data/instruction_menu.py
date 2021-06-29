import random
import arcade
from arcade.gui import UIManager
from data import constants

class Instruction_Menu(arcade.View):
    """
    An instruction menu
    """

    def __init__(self, pause_view):
        super().__init__()
        self.instruction_view = pause_view

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("INSTRUCTIONS", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+140,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press Esc. to return",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2+90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("The goal of the game is to not die from being obese or underweight",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2+30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press W to move up, S to move down",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press A to move left, D to move right",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-60,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Gather unhealthy foods to increase your weight",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-90,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Gather healthy foods to decrease your weight",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-120,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
    
    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.instruction_view)