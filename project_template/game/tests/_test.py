""" -- Test File --

Class: n/a

Functions:  test_constants()
            test_game()
"""
import arcade
import os
import random
from typing import cast

from arcade.window_commands import set_window

from data import constants, food_sprite
from data.game import End_Menu
from data.game import FoodSprite
from data.game import Game
# from data.game import Instruction_Menu
from data.game import Pause_Menu
from data.game import PlayerSprite
# from data.game import Start_Menu
from data.game import TurningSprite
from data.game import Win_Menu

def test_constants():
    """ Test code for the constants file

        Args: n/a
    """
    assert constants.SCREEN_WIDTH == 800
    assert constants.STARTING_food_COUNT == 10
    assert constants.SCALE == 0.5
    assert constants.OFFSCREEN_SPACE == 10
    assert constants.SCREEN_WIDTH == 800
    assert constants.SCREEN_HEIGHT == 600
    assert constants.SCREEN_TITLE == "Food Smasher"
    assert constants.LEFT_LIMIT == -constants.OFFSCREEN_SPACE
    assert constants.RIGHT_LIMIT == constants.SCREEN_WIDTH + constants.OFFSCREEN_SPACE
    assert constants.BOTTOM_LIMIT == -constants.OFFSCREEN_SPACE
    assert constants.TOP_LIMIT == constants.SCREEN_HEIGHT + constants.OFFSCREEN_SPACE
    assert constants.MOVEMENT_SPEED == 5

def test_end_menu():
    """ Test code for the end_menu file

    Args: n/a
    """
    set_window(arcade.View)
    test = End_Menu(arcade.View)
    End_Menu.on_show(test)
    # End_Menu.on_draw(test)
    End_Menu.on_key_press(test, "ESCAPE", "none")
    End_Menu.on_key_press(test, "ENTER", "none")
    assert test.game_view is not None
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None

def test_food_sprite():
    """ Test code for the food_sprite file

    Args: n/a
    """
    # test = FoodSprite(arcade.View, constants.SCALE)
    pass


def test_game():
    """ Test code for the game file

    Args: n/a
    """
    # window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
#     game = Game()
#     # window.show_view(game)
#     # arcade.run()

#     window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
#     start_view = game.Start_Menu()
#  #   window.show_view(start_view)
#     arcade.run()

        # assert game.unhealthy_food_list >= 0
    # assert game.healthy_food_list >= 0
    pass







# # import constants 

# # def test_constants():
# #     assert constants.SCREEN_WIDTH == 7

# # game.py methods
# def test_on_key_press(capsys):
#     file_path = os.path.dirname(os.path.abspath(__file__))
#     os.chdir(file_path)

#     capsys.frame_count = 0

#     capsys.game_over = False

#     capsys.player_sprite_list = arcade.SpriteList()
#     capsys.food_list = arcade.SpriteList()
#     capsys.bullet_list = arcade.SpriteList()
#     capsys.player_life_list = arcade.SpriteList()

#     capsys.score = 0
#     capsys.player_sprite = None
#     capsys.lives = 3

#     capsys.left_pressed = False
#     capsys.right_pressed = False
#     capsys.up_pressed = False
#     capsys.down_pressed = False

#     symbol = arcade.key

#     if  symbol == arcade.key.SPACE:
#         arcade.play_sound(capsys.laser_sound)


#     if symbol == arcade.key.W:
#         capsys.up_pressed = True
#     elif symbol == arcade.key.S:
#         capsys.down_pressed = True
#     elif symbol == arcade.key.A:
#         capsys.left_pressed = True
#     elif symbol == arcade.key.D:
#         capsys.right_pressed = True


#     #tests to see if the user's input matches the direction of the player
#     if symbol == arcade.key.W:
#         assert capsys.up_pressed == True
#         assert capsys.down_pressed == False
#         assert capsys.left_pressed == False
#         assert capsys.right_pressed == False

#     if symbol == arcade.key.S:
#         assert capsys.up_pressed == False
#         assert capsys.down_pressed == True
#         assert capsys.left_pressed == False
#         assert capsys.right_pressed == False

#     if symbol == arcade.key.A:
#         assert capsys.up_pressed == False
#         assert capsys.down_pressed == False
#         assert capsys.left_pressed == True
#         assert capsys.right_pressed == False

#     if symbol == arcade.key.D:
#         assert capsys.up_pressed == False
#         assert capsys.down_pressed == False
#         assert capsys.left_pressed == False
#         assert capsys.right_pressed == True



# def test_on_key_release(capsys):

    
#     symbol = arcade.key
#     if symbol == arcade.key.W:
#         capsys.up_pressed = False
#     elif symbol == arcade.key.S:
#         capsys.down_pressed = False
#     elif symbol == arcade.key.A:
#         capsys.left_pressed = False
#     elif symbol == arcade.key.D:
#         capsys.right_pressed = False

#     #test to see if keyboard controls are functional
#     if symbol == arcade.key.W:
#         assert capsys.up_pressed == False
#     if symbol == arcade.key.S:
#         assert capsys.down_pressed == False
#     if symbol == arcade.key.A:
#         assert capsys.left_pressed == False
#     if symbol == arcade.key.D:
#         assert capsys.right_pressed == False


# def test_on_update(capsys):
#     capsys.left_pressed = False
#     capsys.right_pressed = False
#     capsys.up_pressed = False
#     capsys.down_pressed = False

#     capsys.change_x = 0
#     capsys.change_y = 0

#     if capsys.up_pressed and capsys.down_pressed == False:
#         capsys.pchange_y = 5
#     elif capsys.down_pressed == True and capsys.up_pressed == False:
#         capsys.change_y = -5
#     if capsys.left_pressed == True and capsys.right_pressed == False:
#         capsys.change_x = -5
#     elif capsys.right_pressed == True and capsys.left_pressed == False:
#         capsys.change_x = 5
    
#     capsys.food = 'food'
#     capsys.lives = 3
#     foods = capsys.food
#     if len(foods) > 0:
#         if capsys.lives > 0:
#             capsys.lives -= 1
#             print("Crash")
#         else:
#             capsys.game_over = True
#             print("Game over")

#     #test to see if diagonal motion is functional
#     if capsys.up_pressed and not capsys.down_pressed:
#         assert capsys.change_y == 5
#     if capsys.down_pressed and not capsys.up_pressed:
#         assert capsys.change_y == -5
#     if capsys.left_pressed and not capsys.right_pressed:
#         assert capsys.change_x == -5
#     if capsys.right_pressed and not capsys.left_pressed:
#         assert capsys.change_x == 5

#     #test to see if user loses a life when colliding with an object
#     capsys.lives = 3
#     if len(foods) > 0:
#         capsys.lives -= 1
    
#     assert capsys.lives == 2
    
#     #test to see if the game is over when user has no more lives
#     if len(foods) < 0:
#         assert capsys.game_over == True

# # player_sprite.py methods
# def test_update(capsys):
#     capsys.respawning = 0

#     if capsys.respawning:
#         capsys.respawning += 1
#         capsys.alpha = capsys.respawning
#         if capsys.respawning > 250:
#             capsys.respawning = 0
#             capsys.alpha = 255

#     capsys.right = 0
#     capsys.left = 0
#     capsys.bottom = 0
#     capsys.top = 0

#     if capsys.right < 0:
#         capsys.left = 800

#     if capsys.left > 800:
#         capsys.right = 0

#     if capsys.bottom < 0:
#         capsys.top = 600

#     if capsys.top > 600:
#         capsys.bottom = 0

#     #test to see if the character appears on the other side of the screen when going off screen
#     capsys.right == 0
#     if capsys.right < 0:
#         assert capsys.left == 800

#     capsys.left = 801
#     if capsys.left > 800:
#         assert capsys.right == 0

#     capsys.bottom = 0
#     if capsys.bottom < 0:
#         assert capsys.top == 600

#     capsys.top = 601
#     if capsys.top > 600:
#         assert capsys.bottom == 0


    
    