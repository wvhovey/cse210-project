""" -- Start Menu File --

Class: Start_Menu()

Functions:  __init__()
            on_draw()
            on_show_view()
            setup()
            on_button_click1()
            on_button_click2()
"""

import random
import arcade
from arcade.gui import UIManager
from data.game import Game
from data.instruction_menu import Instruction_Menu
from data import constants
import time

MUSIC_VOLUME = 0.5

class Start_Menu(arcade.View):
    """ This class creates the Start menu when the program begins.

    Stereotype:
        Information Holder

    Attributes:
        view (Null): holds the starting menu view.
        ui_manager(UIManager): manages the ui and the starting menu buttons.

    """

    def __init__(self):
        """ The class constructor.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """ 
        super().__init__()

        self.ui_manager = UIManager()
        self.view = None

        # Music
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None

    def play_song(self):

        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)

        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)
        time.sleep(0.3)

    def on_draw(self):
        """ Renders the start menu with the correct ui.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """  
        arcade.start_render()
        self.ui_manager.on_draw()

    def on_show_view(self):
        """ Sets the background color of the Start menu.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """  
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Creates the view for the Start menu.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """  
        self.ui_manager.purge_ui_elements()

        # self.song1 = constants.assets_dir / "sounds" / "25_Battle of Stoicism.mp3"
        self.song1 = constants.assets_dir / "sounds" / "068 - Slow and Steady.mp3"
        self.music_list = [self.song1]
        self.current_song_index = 0
        self.play_song()

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
            center_x = middle,
            center_y = y_slot * 1,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'New Game'
        )
        self.ui_manager.add_ui_element(self.button2)

        self.button1 = arcade.gui.UIImageButton(
            center_x = middle,
            center_y = y_slot * 2,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'Instructions'
        )
        self.ui_manager.add_ui_element(self.button1)

        self.button1.on_click = self.on_button_click1
        self.button2.on_click = self.on_button_click2

    def on_button_click1(self):
        """ Allows the user to click a button to view the instruction menu.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """  
        self.music.stop(self.current_player)
        self.ui_manager.purge_ui_elements()
        instruction = Instruction_Menu(self)
        self.window.show_view(instruction)
    
    def on_button_click2(self):
        """ Allows the user to click a button to begin the game.
        
        Args:
            self (Start_Menu): an instance of Start_Menu.
        """
        self.music.stop(self.current_player)
        self.ui_manager.purge_ui_elements()
        game = Game()
        game.start_new_game()
        self.window.show_view(game)
