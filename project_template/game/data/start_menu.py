import random
import arcade
from arcade.gui import UIManager
from data.game import Game
from data.instruction_menu import Instruction_Menu


class Start_Menu(arcade.View):
    """
    Starting view when the program begins
    """

    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()
        self.view = None

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()
        self.ui_manager.on_draw()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

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
        self.button2 = arcade.gui.UIImageButton(
            center_x=middle,
            center_y=y_slot * 1,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='New Game'
        )
        self.ui_manager.add_ui_element(self.button2)

        self.button1 = arcade.gui.UIImageButton(
            center_x=middle,
            center_y=y_slot * 2,
            normal_texture=button_normal,
            hover_texture=hovered_texture,
            press_texture=pressed_texture,
            text='Instructions'
        )
        self.ui_manager.add_ui_element(self.button1)

        self.button1.on_click = self.on_button_click1
        self.button2.on_click = self.on_button_click2

    def on_button_click1(self):
        self.ui_manager.purge_ui_elements()
        instruction = Instruction_Menu(self)
        self.window.show_view(instruction)

    def on_button_click2(self):
        self.ui_manager.purge_ui_elements()
        game = Game()
        game.start_new_game()
        self.window.show_view(game)
