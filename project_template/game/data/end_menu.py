import random
import arcade
from arcade.gui import UIManager
from data import constants

class End_Menu(arcade.View):
    """
    The end screen menu, you can either quit or restart
    """
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to quit",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to restart the game",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # end game
            self.window.close_window()
        elif key == arcade.key.ENTER:  # restart game
            self.game_view.start_new_game()
            self.window.show_view(self.game_view)