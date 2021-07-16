""" -- end menu file --

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
import time

music_volume = 0.3

class end_menu(arcade.View):
    """ this class creates the end menu when an end condition is met or the player ends the game.
    
    stereotype:
        information holder

    attributes:
        game_view (object): holds the information for the current game view.

    """
    def __init__(self, game_view):
        """ the class constructor.
        
        args:
            self (end_menu): an instance of end_menu.
            game_view (object): an instance of game_view.
        """        
        super().__init__()
        self.game_view = game_view
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

    def on_show(self):
        """ sets the background color of the end menu.
        
        args:
            self (end_menu): an instance of end_menu.
        """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.song1 = constants.assets_dir / "sounds" / "20_in sorrow.mp3"
        self.music_list = [self.song1]
        self.current_song_index = 0
        self.play_song()

    def on_draw(self):
        """ creates the view for the end menu.
        
        args:
            self (end_menu): an instance of end_menu.
        """    
        arcade.start_render()

        arcade.draw_text("game over", self.window.width/2, self.window.height/2+50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        # show tip to return or reset
        arcade.draw_text("press esc. to quit",
                         self.window.width/2,
                         self.window.height/2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("press enter to restart the game",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ allows the user to end or resume the game on key press.
        
        args:
            self (end_menu): an instance of end_menu.
            key (arcade.key): sets the keys to end or resume the game.
        """  
        if key == arcade.key.ESCAPE:   # end game
            self.window.close()
        elif key == arcade.key.ENTER:  # restart game
            self.music.stop(self.current_player)
            self.game_view.start_new_game()
            self.window.show_view(self.game_view)