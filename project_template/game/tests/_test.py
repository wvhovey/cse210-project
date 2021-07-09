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
from data.end_menu import End_Menu
from data.food_sprite import FoodSprite
from data.game import Game
from data.instruction_menu import Instruction_Menu
from data.pause_menu import Pause_Menu
from data.player_sprite import PlayerSprite
from data.start_menu import Start_Menu
from data.turning_sprite import TurningSprite
from data.win_menu import Win_Menu

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




# ------- IGNORE THIS ------: It is for Debugging and used by Knighten,
# I will delete it when I no longer need it, Thanks! :)

# window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
# test = Game()
# print(len(test.player_sprite_list))
# print(len(test.healthy_food_list))
# print(len(test.unhealthy_food_list))
# print(len(test.player_life_list))

# test.start_new_game()
# print("space sdlkfjsdlk")
# print(len(test.player_sprite_list))
# print(len(test.healthy_food_list))
# print(len(test.unhealthy_food_list))
# print(len(test.player_life_list))





def test_game():
    """ Test code for the game file

    Args: n/a
    """
    # window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    test = Game()
     # window.show_view(game)
     # arcade.run()

    # window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    # start_view = game.Start_Menu()
 #   window.show_view(start_view)
    # arcade.run()

    # test initilized variables
    assert test.frame_count == 0
    assert test.player_scale == 0.5
    assert test.game_over == False

    # test Sprite lists
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None
    assert test.player_life_list is not None
    # test Sprite lists are the correct lengths
    assert len(test.player_sprite_list) == 0
    assert len(test.healthy_food_list) == 0
    assert len(test.unhealthy_food_list) == 0
    assert len(test.player_life_list) == 0

    # test Set up the player
    assert test.weight == 250
    assert test.player_sprite == None

    # test that variables for key presses are correct
    assert test.left_pressed == False
    assert test.right_pressed == False
    assert test.up_pressed == False
    assert test.down_pressed == False

    # test Sounds
    assert test.laser_sound is not None
    assert test.hit_sound1 is not None
    assert test.hit_sound2 is not None
    assert test.hit_sound3 is not None
    assert test.hit_sound4 is not None


    # call start_new_game function
    test.start_new_game()

    # Test everything is set up
    assert test.frame_count == 0
    assert test.game_over == False
    assert test.left_pressed == False
    assert test.right_pressed == False
    assert test.up_pressed == False
    assert test.down_pressed == False

    # test Sprite lists still exist
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None
    assert test.player_life_list is not None

    # test Sprite lists to see if they are no longer zero because start_new_game() was called
    assert len(test.player_sprite_list) == 1
    assert len(test.healthy_food_list) == constants.STARTING_food_COUNT
    assert len(test.unhealthy_food_list) == constants.STARTING_food_COUNT
    assert len(test.player_life_list) == 3

    # test Set up the player
    assert test.weight == 250
    assert test.player_sprite is not None
    assert test.lives == 3


    # Need to set up parameterized test for the following to test all options:
    # symbol = arcade.key.W
    # if symbol == arcade.key.W:
    #     test.up_pressed = True
    # elif symbol == arcade.key.S:
    #     test.down_pressed = True
    # elif symbol == arcade.key.A:
    #     test.left_pressed = True
    # elif symbol == arcade.key.D:
    #     test.right_pressed = True

    # test.on_key_press()





def test_instruction_menu():
    """ Test code for the instruction_menu file

    Args: n/a
    """
    set_window(arcade.View)
    test = Instruction_Menu(arcade.View)
    Instruction_Menu.on_show(test)
    # Instruction_Menu.on_draw(test)
    Instruction_Menu.on_key_press(test, "ESCAPE", "none")
    Instruction_Menu.on_key_press(test, "ENTER", "none")
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None    


def test_pause_menu():
    """ Test code for the pause_menu file

    Args: n/a
    """
    set_window(arcade.View)
    # test = Pause_Menu(arcade.View)
    # Pause_Menu.on_show(test)
    # Pause_Menu.on_draw(test)
    # Pause_Menu.on_key_press(test, "ESCAPE", "none")
    # Pause_Menu.on_key_press(test, "ENTER", "none")
    # assert test.window is not None
    # assert test.__doc__ is not None
    # assert test.key is None   

def test_player_sprite():
    """ Test code for the player_sprite file

    Args: n/a
    """
    set_window(arcade.Sprite)
    #test = PlayerSprite("cake.png", constants.SCALE)
    # PlayerSprite.on_show(test)
    # PlayerSprite.on_draw(test)
    # PlayerSprite.on_key_press(test, "ESCAPE", "none")
    # PlayerSprite.on_key_press(test, "ENTER", "none")
    # assert test.window is not None
    # assert test.__doc__ is not None
    # assert test.key is None 


def test_start_menu():
    """ Test code for the start_menu file

    Args: n/a
    """
    set_window(arcade.View)
    # test = Start_Menu()
    # Start_Menu.on_show(test)
    # Start_Menu.on_draw(test)
    # Start_Menu.on_key_press(test, "ESCAPE", "none")
    # Start_Menu.on_key_press(test, "ENTER", "none")
    # assert test.window is not None
    # assert test.__doc__ is not None
    # assert test.key is None 



def test_turning_sprite(): # MAYBE DELETE.... I DON"T THINK WE USE THIS
    """ Test code for the turning_sprite file

    Args: n/a
    """
    # set_window(arcade.Sprite)
    #test = PlayerSprite("cake.png", constants.SCALE)
    # PlayerSprite.on_show(test)
    # PlayerSprite.on_draw(test)
    # PlayerSprite.on_key_press(test, "ESCAPE", "none")
    # PlayerSprite.on_key_press(test, "ENTER", "none")
    # assert test.window is not None
    # assert test.__doc__ is not None
    # assert test.key is None 


def test_win_menu():
    """ Test code for the win_menu file

    Args: n/a
    """
    set_window(arcade.View)
    test = Win_Menu(arcade.View)
    Win_Menu.on_show(test)
    # Win_Menu.on_draw(test)
    # Win_Menu.on_key_press(test, "ESCAPE", "none")
    # StarWin_Menut_Menu.on_key_press(test, "ENTER", "none")
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None 







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


    
    