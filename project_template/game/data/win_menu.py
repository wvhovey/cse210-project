""" -- Win Menu File --

Class: Win_Menu()

Functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import arcade
from arcade.gui import UIManager
from data import constants
import time

MUSIC_VOLUME = 0.5

class Win_Menu(arcade.View):
    """ This class creates the Win menu when a win condition is met.

    Stereotype:
        Information Holder
    
    Args:
        arcade.View (arcade): arcade library.

    Attributes:
        game_view (object): holds the information for the current game view.

    """
    def __init__(self, game_view):
        """ The class constructor.
        
        Args:
            self (Win_Menu): an instance of Win_Menu.
            game_view (object): an instance of game_view.
        """ 
        super().__init__()
        self.game_view = game_view

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

    def on_show(self):
        """ Sets the background color of the Win menu.
        
        Args:
            self (Win_Menu): an instance of Win_Menu.
        """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Creates the view for the Win menu.
        
        Args:
            self (Win_Menu): an instance of Win_Menu.
        """  
        arcade.start_render()
        
        arcade.draw_text("You Won!!", self.window.width/2, self.window.height/2+50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to quit",
                         self.window.width/2,
                         self.window.height/2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to restart the game",
                         self.window.width/2,
                         self.window.height/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def setup(self):

        # plays the winning song.
        self.song1 = constants.assets_dir / "sounds" / "121 The Hall of Fame.mp3"
        self.music_list = [self.song1]
        self.current_song_index = 0
        self.play_song()


    def on_key_press(self, key, _modifiers):
        """ Allows the user to end or restart the game on key press.
        
        Args:
            self (Win_Menu): an instance of Win_Menu.
            key (arcade.key): sets the keys to end or restart the game.
        """   
        if key == arcade.key.ESCAPE:   # end game
            # self.music.stop(self.current_player)
            self.window.close()
        elif key == arcade.key.ENTER:  # restart game
            self.music.stop(self.current_player)
            self.game_view.start_new_game()
            self.window.show_view(self.game_view)