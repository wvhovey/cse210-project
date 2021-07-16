""" -- win menu file --

class: win_menu()

functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import arcade
from arcade.gui import UIManager
from data import constants
import time

music_volume = 0.5

class win_menu(arcade.View):
    """ this class creates the win menu when a win condition is met.

    stereotype:
        information holder
    
    args:
        arcade.view (arcade): arcade library.

    attributes:
        game_view (object): holds the information for the current game view.

    """
    def __init__(self, game_view):
        """ the class constructor.
        
        args:
            self (win_menu): an instance of win_menu.
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
        """ sets the background color of the win menu.
        
        args:
            self (win_menu): an instance of win_menu.
        """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ creates the view for the win menu.
        
        args:
            self (win_menu): an instance of win_menu.
        """  
        arcade.start_render()
        
        arcade.draw_text("you won!!", self.window.width/2, self.window.height/2+50,
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

    def setup(self):

        # plays the winning song.
        self.song1 = constants.assets_dir / "sounds" / "121 the hall of fame.mp3"
        self.music_list = [self.song1]
        self.current_song_index = 0
        self.play_song()


    def on_key_press(self, key, _modifiers):
        """ allows the user to end or restart the game on key press.
        
        args:
            self (win_menu): an instance of win_menu.
            key (arcade.key): sets the keys to end or restart the game.
        """   
        if key == arcade.key.ESCAPE:   # end game
            # self.music.stop(self.current_player)
            self.window.close()
        elif key == arcade.key.ENTER:  # restart game
            self.music.stop(self.current_player)
            self.game_view.start_new_game()
            self.window.show_view(self.game_view)