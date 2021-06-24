import random
import arcade
from arcade.gui import UIManager

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Implement Views Example"


class Start_Menu(arcade.View):
    """
    Main view. Really the only view in this example. """

    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()
        self.ui_manager.on_draw()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        # Makes variables to place the buttons
        y_slot = self.window.height // 3
        middle = self.window.width // 2

        # Creates the textures and button interactions.
        button_normal = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_normal.png')
        hovered_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_hover.png')
        pressed_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_press.png')

        # Creates the buttons.
        button1 = arcade.gui.UIImageButton(
            center_x = middle,
            center_y = y_slot * 1,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(button1)

        button2 = arcade.gui.UIImageButton(
            center_x = middle,
            center_y = y_slot * 2,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Instructions'
        )
        self.ui_manager.add_ui_element(button2)

def main():
    """ Main method """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Start_Menu()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
