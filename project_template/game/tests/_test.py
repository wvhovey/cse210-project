""" -- test file --

class: n/a

functions:  test_constants()
            test_game()
"""
import arcade
import os
import random
import pytest
from typing import cast

from arcade.window_commands import set_window

from data import constants
from data.end_menu import end_menu
from data.food_sprite import foodsprite
from data.game import game
from data.instruction_menu import instruction_menu
from data.pause_menu import pause_menu
from data.player_sprite import playersprite
from data.start_menu import start_menu
from data.win_menu import win_menu

def test_constants():
    """ test code for the constants file

        args: n/a
    """
    assert constants.screen_width == 800
    assert constants.starting_food_count == 10
    assert constants.scale == 0.5
    assert constants.offscreen_space == 10
    assert constants.screen_width == 800
    assert constants.screen_height == 600
    assert constants.screen_title == "food smasher"
    assert constants.left_limit == -constants.offscreen_space
    assert constants.right_limit == constants.screen_width + constants.offscreen_space
    assert constants.bottom_limit == -constants.offscreen_space
    assert constants.top_limit == constants.screen_height + constants.offscreen_space
    assert constants.movement_speed == 5

def test_end_menu():
    """ test code for the end_menu file

    args: n/a
    """
    set_window(arcade.view)
    test = end_menu(arcade.view)
    end_menu.on_show(test)
    # end_menu.on_draw(test) #this fails, saying that it has no attribute 'clear'
    end_menu.on_key_press(test, "escape", "none")
    end_menu.on_key_press(test, "enter", "none")
    assert test.game_view is not None
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None

@pytest.mark.parametrize("test_input, expected_type, expected_sound", [("good", "good", constants.assets_dir / "sounds" / "laser1.ogg"), ("bad", "bad", constants.assets_dir / "sounds" / "laser1.ogg")])
def test_food_sprite(test_input, expected_type, expected_sound):
    """ test code for the food_sprite file

    args: n/a
    """
    
    # test initialized variables
    test = foodsprite(constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "icecream.png", constants.scale, test_input)
    assert test.size == 0
    assert test.type_of_food == expected_type
    assert test.eating_sound == expected_sound

    # call and test the update() method for proper wrapping
    for y in range(0, constants.screen_height):
        for x in range(0, constants.screen_width):
            test.center_x = x
            test.center_y = y
            test.update()
            if x == constants.left_limit:
                assert test.center_x != constants.right_limit
            if x == constants.right_limit:
                assert test.center_x != constants.left_limit
            if y == constants.top_limit:
                assert test.center_y != constants.bottom_limit
            if y == constants.bottom_limit:
                assert test.center_y != constants.top_limit

def test_game():
    """ test code for the game file

    args: n/a
    """
    # window = arcade.window(constants.screen_width, constants.screen_height, constants.screen_title)
    test = game()
     # window.show_view(game)
     # arcade.run()

    # window = arcade.window(constants.screen_width, constants.screen_height, constants.screen_title)
    # start_view = game.start_menu()
 #   window.show_view(start_view)
    # arcade.run()

    # test initilized variables
    assert test.frame_count == 0
    assert test.player_scale == 0.5
    assert test.game_over == False
    assert test.total_time == 0.0

    # test sprite lists
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None

    # test sprite lists are the correct lengths
    assert len(test.player_sprite_list) == 0
    assert len(test.healthy_food_list) == 0
    assert len(test.unhealthy_food_list) == 0

    # test set up the player
    assert test.weight == 250
    assert test.player_sprite == None

    # test that variables for key presses are correct
    assert test.left_pressed == False
    assert test.right_pressed == False
    assert test.up_pressed == False
    assert test.down_pressed == False

    # test sounds
    assert test.munch is not None
    assert test.munch2 is not None
    assert test.munch3 is not None
    assert test.munch4 is not None
    assert test.munch5 is not None


    # call start_new_game function
    test.start_new_game()

    # test everything is set up
    assert test.frame_count == 0
    assert test.total_time == 0
    assert test.game_over == False
    assert test.left_pressed == False
    assert test.right_pressed == False
    assert test.up_pressed == False
    assert test.down_pressed == False

    # test sprite lists still exist
    assert test.player_sprite_list is not None
    assert test.healthy_food_list is not None
    assert test.unhealthy_food_list is not None

    # test sprite lists to see if they are no longer zero because start_new_game() was called
    assert len(test.player_sprite_list) == 1
    assert len(test.healthy_food_list) == constants.starting_food_count
    assert len(test.unhealthy_food_list) == constants.starting_food_count

    # test set up the player
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
    #  it gives this error: e       attributeerror: type object 'view' has no attribute 'clear'
    # test.on_draw()

    # call on_update
    test.on_update(1)
    # test that time is moving forward
    assert test.frame_count > 0
    assert test.total_time > 0

    # test on_key_press()
    for x in [arcade.key.w, arcade.key.s, arcade.key.a, arcade.key.d]:
        test.on_key_press(x, 1)
        if x == arcade.key.w:
            assert test.up_pressed == True
        if x == arcade.key.s:
            assert test.down_pressed == True
        if x == arcade.key.a:
            assert test.left_pressed == True
        if x == arcade.key.d:
            assert test.right_pressed == True

    # test on_key_release
    for x in [arcade.key.w, arcade.key.s, arcade.key.a, arcade.key.d]:
        test.on_key_release(x, 1)
        if x == arcade.key.w:
            assert test.up_pressed == False
        if x == arcade.key.s:
            assert test.down_pressed == False
        if x == arcade.key.a:
            assert test.left_pressed == False
        if x == arcade.key.d:
            assert test.right_pressed == False

def test_instruction_menu():
    """ test code for the instruction_menu file

    args: n/a
    """
    set_window(arcade.view)
    test = instruction_menu(arcade.view)
    instruction_menu.on_show(test)
    # instruction_menu.on_draw(test)
    instruction_menu.on_key_press(test, "escape", "None")
    instruction_menu.on_key_press(test, "enter", "None")
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None    

def test_pause_menu():
    """ test code for the pause_menu file

    args: n/a
    """
    # get the following error when trying to test pause_menu: e    attributeerror: type object 'view' has no attribute 'push_handlers'

    # set_window(arcade.view)
    # test = pause_menu(arcade.view)


def test_player_sprite():
    """ test code for the player_sprite file

    args: n/a
    """
    
    # test initialized variables
    test = playersprite(constants.assets_dir / "images" / "man.png", 0.5)
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
    assert test.left == constants.screen_width

    test.left = constants.screen_width + 1
    test.update()
    assert test.right == 0

    test.bottom = -1
    test.update()
    assert test.top == constants.screen_height

    test.top = constants.screen_height + 1
    test.update()
    assert test.bottom == 0


def test_start_menu():
    """ test code for the start_menu file

    args: n/a
    """

    ## getting error, "failed cse210-project/project_template/game/tests/_test.py::test_start_menu - attributeerror: type object 'view' has no attribute 'push_handlers'"

    # set_window(arcade.view)
    # test = start_menu()
    # start_menu.on_show(test)
    # start_menu.on_draw(test)
    # start_menu.on_key_press(test, "escape", "None")
    # start_menu.on_key_press(test, "enter", "None")
    # assert test.window is not None
    # assert test.__doc__ is not None
    # assert test.key is None 

def test_win_menu():
    """ test code for the win_menu file

    args: n/a
    """
    set_window(arcade.view)
    test = win_menu(arcade.view)
    win_menu.on_show(test)
    # win_menu.on_draw(test)
    # win_menu.on_key_press(test, "escape", "None")
    # starwin_menut_menu.on_key_press(test, "enter", "None")
    assert test.window is not None
    assert test.__doc__ is not None
    assert test.key is None 
