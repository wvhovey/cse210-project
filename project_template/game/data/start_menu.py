""" -- start menu file --

class: start_menu()

functions:  __init__()
            on_draw()
            on_show_view()
            setup()
            on_button_click1()
            on_button_click2()
"""

import random
import arcade
from arcade.gui import UIManager
from data.game import game
from data.instruction_menu import instruction_menu
from data import constants
import time

music_volume = 0.5

class start_menu(arcade.View):
    """ this class creates the start menu when the program begins.

    stereotype:
        information holder

    attributes:
        view (null): holds the starting menu view.
        ui_manager(UIManager): manages the ui and the starting menu buttons.

    """

    def __init__(self):
        """ the class constructor.
        
        args:
            self (start_menu): an instance of start_menu.
        """ 
        super().__init__()

        self.ui_manager = UIManager()
        self.view = None

        # music
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None

    def play_song(self):

        """ play the song. """
        # stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)

        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(music_volume)
        time.sleep(0.3)

    def on_draw(self):
        """ renders the start menu with the correct ui.
        
        args:
            self (start_menu): an instance of start_menu.
        """  
        arcade.start_render()
        self.ui_manager.on_draw()

    def on_show_view(self):
        """ sets the background color of the start menu.
        
        args:
            self (start_menu): an instance of start_menu.
        """  
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ creates the view for the start menu.
        
        args:
            self (start_menu): an instance of start_menu.
        """  
        self.ui_manager.purge_ui_elements()

        # self.song1 = constants.assets_dir / "sounds" / "25_battle of stoicism.mp3"
        self.song1 = constants.assets_dir / "sounds" / "068 - slow and steady.mp3"
        self.music_list = [self.song1]
        self.current_song_index = 0
        self.play_song()

        # makes variables to place the buttons
        y_slot = self.window.height // 3
        middle = self.window.width // 2

        # creates the textures and button interactions.
        button_normal = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_normal.png')
        hovered_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_hover.png')
        pressed_texture = arcade.load_texture(
            ':resources:gui_basic_assets/red_button_press.png')

        # creates the buttons.
        self.button2 = arcade.gui.UIImageButton(
            center_x = middle,
            center_y = y_slot * 1,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'new game'
        )
        self.ui_manager.add_ui_element(self.button2)

        self.button1 = arcade.gui.UIImageButton(
            center_x = middle,
            center_y = y_slot * 2,
            normal_texture = button_normal,
            hover_texture = hovered_texture,
            press_texture = pressed_texture,
            text = 'instructions'
        )
        self.ui_manager.add_ui_element(self.button1)

        self.button1.on_click = self.on_button_click1
        self.button2.on_click = self.on_button_click2

    def on_button_click1(self):
        """ allows the user to click a button to view the instruction menu.
        
        args:
            self (start_menu): an instance of start_menu.
        """  
        self.music.stop(self.current_player)
        self.ui_manager.purge_ui_elements()
        instruction = instruction_menu(self)
        self.window.show_view(instruction)
    
    def on_button_click2(self):
        """ allows the user to click a button to begin the game.
        
        args:
            self (start_menu): an instance of start_menu.
        """
        self.music.stop(self.current_player)
        self.ui_manager.purge_ui_elements()
        game2 = game()
        game2.start_new_game()
        self.window.show_view(game2)
