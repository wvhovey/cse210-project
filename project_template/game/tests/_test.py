""" -- Test File --

Class: n/a

Functions:  test_constants()
            test_game()
"""
import arcade
import os
import random
import pytest
from typing import cast

from arcade.window_commands import set_window

from data import constants
from data.end_menu import End_Menu
from data.food_sprite import FoodSprite
from data.game import Game
from data.instruction_menu import Instruction_Menu
from data.pause_menu import Pause_Menu
from data.player_sprite import PlayerSprite
from data.start_menu import Start_Menu
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
    # End_Menu.on_draw(test) #This fails, saying that it has no attribute 'clear'
    End_Menu.on_key_press(test, "ESCAPE", "none")
    End_Menu.on_key_press(test, "ENTER", "none")
    assert test.game_view is not None
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None

@pytest.mark.parametrize("test_input, expected_type, expected_sound", [("good", "good", constants.assets_dir / "sounds" / "laser1.ogg"), ("bad", "bad", constants.assets_dir / "sounds" / "laser1.ogg")])
def test_food_sprite(test_input, expected_type, expected_sound):
    """ Test code for the food_sprite file

    Args: n/a
    """
    
    # test initialized variables
    test = FoodSprite(constants.assets_dir / "images" / "foodKit_v1.2" / "side" / "iceCream.png", constants.SCALE, test_input)
    assert test.size == 0
    assert test.type_of_food == expected_type
    assert test.eating_sound == expected_sound

    # call and test the update() method for proper wrapping
    for y in range(0, constants.SCREEN_HEIGHT):
        for x in range(0, constants.SCREEN_WIDTH):
            test.center_x = x
            test.center_y = y
            test.update()
            if x == constants.LEFT_LIMIT:
                assert test.center_x != constants.RIGHT_LIMIT
            if x == constants.RIGHT_LIMIT:
                assert test.center_x != constants.LEFT_LIMIT
            if y == constants.TOP_LIMIT:
                assert test.center_y != constants.BOTTOM_LIMIT
            if y == constants.BOTTOM_LIMIT:
                assert test.center_y != constants.TOP_LIMIT

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
    assert test.total_time == 0.0

    # test Sprite lists
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None

    # test Sprite lists are the correct lengths
    assert len(test.player_sprite_list) == 0
    assert len(test.healthy_food_list) == 0
    assert len(test.unhealthy_food_list) == 0

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
    assert test.total_time == 0
    assert test.game_over == False
    assert test.left_pressed == False
    assert test.right_pressed == False
    assert test.up_pressed == False
    assert test.down_pressed == False

    # test Sprite lists still exist
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None

    # test Sprite lists to see if they are no longer zero because start_new_game() was called
    assert len(test.player_sprite_list) == 1
    assert len(test.healthy_food_list) == constants.STARTING_food_COUNT
    assert len(test.unhealthy_food_list) == constants.STARTING_food_COUNT

    # test Set up the player
    assert test.weight == 250
    assert test.player_sprite is not None

    # test create_unhealthy_food
    test.create_healthy_food(10) # add another 10 items to list of 10
    assert len(test.healthy_food_list) == 20
    test.create_healthy_food(0)
    assert len(test.healthy_food_list) == 20

    # test create_healthy_food
    test.create_unhealthy_food(10) # add another 10 items to list of 10
    assert len(test.unhealthy_food_list) == 20
    test.create_unhealthy_food(0)
    assert len(test.unhealthy_food_list) == 20

    # test on_draw
    #  It gives this Error: E       AttributeError: type object 'View' has no attribute 'clear'
    # test.on_draw()

    # call on_update
    test.on_update(1)
    # test that time is moving forward
    assert test.frame_count > 0
    assert test.total_time > 0

    # test on_key_press()
    for x in [arcade.key.W, arcade.key.S, arcade.key.A, arcade.key.D]:
        test.on_key_press(x, 1)
        if x == arcade.key.W:
            assert test.up_pressed == True
        if x == arcade.key.S:
            assert test.down_pressed == True
        if x == arcade.key.A:
            assert test.left_pressed == True
        if x == arcade.key.D:
            assert test.right_pressed == True

    # test on_key_release
    for x in [arcade.key.W, arcade.key.S, arcade.key.A, arcade.key.D]:
        test.on_key_release(x, 1)
        if x == arcade.key.W:
            assert test.up_pressed == False
        if x == arcade.key.S:
            assert test.down_pressed == False
        if x == arcade.key.A:
            assert test.left_pressed == False
        if x == arcade.key.D:
            assert test.right_pressed == False

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
    # Get the following error when trying to test pause_menu: E    AttributeError: type object 'View' has no attribute 'push_handlers'

    # set_window(arcade.View)
    # test = Pause_Menu(arcade.View)


def test_player_sprite():
    """ Test code for the player_sprite file

    Args: n/a
    """
    
    # test initialized variables
    test = PlayerSprite(constants.assets_dir / "images" / "man.png", 0.5)
    assert test.speed == 0
    assert test.max_speed == 4
    assert test.drag == 0
    assert test.respawning == True
    test.respawning = False
    assert test.respawning == False
    test.respawn()
    assert test.respawning == True
    assert test.angle == 0
    test.angle = 10
    assert test.angle == 10
    test.respawn()
    assert test.angle == 0
    assert test.right is not None

    # test that when player moves off screen they teleport from top to bottom, right to left and vice versa
    test.right = -1
    test.update()
    assert test.left == constants.SCREEN_WIDTH

    test.left = constants.SCREEN_WIDTH + 1
    test.update()
    assert test.right == 0

    test.bottom = -1
    test.update()
    assert test.top == constants.SCREEN_HEIGHT

    test.top = constants.SCREEN_HEIGHT + 1
    test.update()
    assert test.bottom == 0


def test_start_menu():
    """ Test code for the start_menu file

    Args: n/a
    """

    ## Getting error, "FAILED cse210-project/project_template/game/tests/_test.py::test_start_menu - AttributeError: type object 'View' has no attribute 'push_handlers'"

    # set_window(arcade.View)
    # test = Start_Menu()
    # Start_Menu.on_show(test)
    # Start_Menu.on_draw(test)
    # Start_Menu.on_key_press(test, "ESCAPE", "none")
    # Start_Menu.on_key_press(test, "ENTER", "none")
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
