"""
food eater

Shoot cake in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

"""
import random
import math
import arcade
import os

from typing import cast
from data import constants
from data.food_sprite import FoodSprite
from data.player_sprite import PlayerSprite
from data.turning_sprite import TurningSprite
from data.pause_menu import Pause_Menu
from data.end_menu import End_Menu

class Game(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0
        self.player_scale = 0.5
        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.healthy_food_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_life_list = arcade.SpriteList()

        # Set up the player
        self.weight = 250
        self.player_sprite = None
        # self.lives = 3

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Sounds
        self.laser_sound = arcade.load_sound("../assets/sounds/laser1.ogg")
        self.hit_sound1 = arcade.load_sound("../assets/sounds/laser1.ogg")
        self.hit_sound2 = arcade.load_sound("../assets/sounds/laser1.ogg")
        self.hit_sound3 = arcade.load_sound("../assets/sounds/laser1.ogg")
        self.hit_sound4 = arcade.load_sound("../assets/sounds/laser1.ogg")

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        self.frame_count = 0
        self.game_over = False

        arcade.set_background_color(arcade.color.AMAZON) 

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.healthy_food_list = arcade.SpriteList()
        self.unhealthy_food_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_life_list = arcade.SpriteList()

        # Set up the player
        self.weight = 250
        self.player_sprite = PlayerSprite("../assets/images/man.png", self.player_scale)
        self.player_sprite_list.append(self.player_sprite)
        self.lives = 3

        # Set up the little icons that represent the player lives.
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite("../assets/images/man.png", constants.SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.player_life_list.append(life)

        # Make the unhealthy foods
        image_list = ("../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png")

        for i in range(constants.STARTING_food_COUNT):
            image_no = random.randrange(10)
            food_sprite = FoodSprite(image_list[image_no], constants.SCALE)
            food_sprite.guid = "food"

            food_sprite.center_y = random.randrange(constants.BOTTOM_LIMIT, constants.TOP_LIMIT)
            food_sprite.center_x = random.randrange(constants.LEFT_LIMIT, constants.RIGHT_LIMIT)

            food_sprite.change_x = random.random() * 2 - 1
            food_sprite.change_y = random.random() * 2 - 1

            food_sprite.change_angle = (random.random() - 0.5) * 2
            food_sprite.size = 4
            self.unhealthy_food_list.append(food_sprite)

        # Make the healthy foods
        image_list = ("../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png",
                      "../assets/images/salad.png")

        for i in range(constants.STARTING_food_COUNT):
            image_no = random.randrange(10)
            food_sprite = FoodSprite(image_list[image_no], constants.SCALE)
            food_sprite.guid = "food"

            food_sprite.center_y = random.randrange(constants.BOTTOM_LIMIT, constants.TOP_LIMIT)
            food_sprite.center_x = random.randrange(constants.LEFT_LIMIT, constants.RIGHT_LIMIT)

            food_sprite.change_x = random.random() * 2 - 1
            food_sprite.change_y = random.random() * 2 - 1

            food_sprite.change_angle = (random.random() - 0.5) * 2
            food_sprite.size = 4
            self.healthy_food_list.append(food_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.healthy_food_list.draw()
        self.unhealthy_food_list.draw()
        self.player_life_list.draw()
        self.bullet_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Weight: {self.weight}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        output = f"food Count: {len(self.healthy_food_list)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)



    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        
        if symbol == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = Pause_Menu(self)
            self.window.show_view(pause)

        if symbol == arcade.key.W:
            self.up_pressed = True
        elif symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.A:
            self.left_pressed = True
        elif symbol == arcade.key.D:
            self.right_pressed = True

        # if symbol == arcade.key.A:
        #     # self.player_sprite.change_angle = 3
        #     self.player_sprite.speed = 4
        #     self.player_sprite.angle = 90

        # elif symbol == arcade.key.D:
        #     # self.player_sprite.change_angle = -3
        #     self.player_sprite.speed = 4
        #     self.player_sprite.angle = -90

        # elif symbol == arcade.key.W:
        #     self.player_sprite.speed = 4 
        #     self.player_sprite.angle = 0

        # elif symbol == arcade.key.S:
        #     self.player_sprite.speed = 4 
        #     self.player_sprite.angle = 180
        
        # elif symbol == arcade.key.A:
        #     # self.player_sprite.change_angle = 3
        #     self.player_sprite.speed = 4
        #     self.player_sprite.angle = 90

        # elif symbol == arcade.key.D:
        #     # self.player_sprite.change_angle = -3
        #     self.player_sprite.speed = 4
        #     self.player_sprite.angle = -90

        # elif symbol == arcade.key.W:
        #     self.player_sprite.speed = 4 
        #     self.player_sprite.angle = 0

        # elif symbol == arcade.key.S:
        #     self.player_sprite.speed = 4 
        #     self.player_sprite.angle = 180


    def on_key_release(self, symbol, modifiers):
        """ Called whenever a key is released. """
        # if symbol == arcade.key.LEFT:
        #     self.player_sprite.speed = 0
        # elif symbol == arcade.key.RIGHT:
        #     self.player_sprite.speed = 0
        # elif symbol == arcade.key.UP:
        #     self.player_sprite.speed = 0 
        # elif symbol == arcade.key.DOWN:
        #     self.player_sprite.speed = 0  
        # elif symbol == arcade.key.A:
        #     self.player_sprite.speed = 0
        # elif symbol == arcade.key.D:
        #     self.player_sprite.speed = 0
        # elif symbol == arcade.key.W:
        #     self.player_sprite.speed = 0 
        # elif symbol == arcade.key.S:
        #     self.player_sprite.speed = 0  
        if symbol == arcade.key.W:
            self.up_pressed = False
        elif symbol == arcade.key.S:
            self.down_pressed = False
        elif symbol == arcade.key.A:
            self.left_pressed = False
        elif symbol == arcade.key.D:
            self.right_pressed = False

    def on_update(self, x):
        """ Move everything """

        self.frame_count += 1

        if not self.game_over:
            self.healthy_food_list.update()
            self.unhealthy_food_list.update()
            self.bullet_list.update()
            self.player_sprite_list.update()



            # for bullet in self.bullet_list:
            #     foods = arcade.check_for_collision_with_list(bullet, self.healthy_food_list)

            #     for food in foods:
            #         food.remove_from_sprite_lists()


            # if not self.player_sprite.respawning:
                            # Calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0


            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = constants.MOVEMENT_SPEED
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -constants.MOVEMENT_SPEED
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -constants.MOVEMENT_SPEED
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = constants.MOVEMENT_SPEED


            # Code that gives player invincibility after getting hit and respawns in center

            # Call update to move the sprite
            # If using a physics engine, call update player to rely on physics engine
            # for movement, and call physics engine here.
            # self.player_sprite_list.update()
            # foods = arcade.check_for_collision_with_list(self.player_sprite, self.healthy_food_list) 
            # if len(foods) > 0:
            #     if self.lives > 0:
            #         # scale the character, remove current sprite, add sprite with new scale,
            #         # append the new sprite to sprite list. <--- Lines 369 - 372
            #         self.player_scale += 0.2
            #         self.player_sprite_list.remove(self.player_sprite)
            #         self.player_sprite = PlayerSprite("../assets/images/man.png", self.player_scale)
            #         self.player_sprite_list.append(self.player_sprite)
            #         self.lives -= 1
            #         self.player_sprite.respawn()
            #         # foods[0].remove_from_sprite_lists()
            #         self.player_life_list.pop().remove_from_sprite_lists()
            #         self.hit_sound3.play()
            #         print("Crash")
            #     else:


            # Code if we want the player to stay in same place after being hit with no invincibility frames
            # code works by increasing the player's height and width if they're hit
            # to easily comment between the two do: highlight everything and press Ctrl + ?/ 

            self.player_sprite_list.update()
            healthy_foods = arcade.check_for_collision_with_list(self.player_sprite, self.healthy_food_list) 
            if len(healthy_foods) > 0:
                if self.lives > 0:
                    self.weight -= 50
                    # self.lives += 1
                    healthy_foods[0].remove_from_sprite_lists()
                    # self.player_life_list.pop().remove_from_sprite_lists()
                    print("Crash")
                    for player in self.player_sprite_list:
                        # player.append_texture(arcade.load_texture("../assets/images/iceCream.png")) # This can be used to change image of player after being hit
                        # player.set_texture(1) # This can be used to change image of player after being hit
                        player.width = player.width / 1.5 # increases player size 
                        player.height = player.height / 1.5 # increases player size
                if self.weight <= 100:

                    self.game_over = True
                    self.player_scale = 0.5
                    print("Game over")
                    # pass self, the current view, to preserve this view's state
                    end = End_Menu(self)
                    self.window.show_view(end)


            unhealthy_foods = arcade.check_for_collision_with_list(self.player_sprite, self.unhealthy_food_list) 
            if len(unhealthy_foods) > 0:
                if self.lives > 0:
                    self.weight += 50
                    # self.lives -= 1
                    unhealthy_foods[0].remove_from_sprite_lists()
                    # self.player_life_list.pop().remove_from_sprite_lists()
                    print("Crash")
                    for player in self.player_sprite_list:
                        # player.append_texture(arcade.load_texture("../assets/images/iceCream.png")) # This can be used to change image of player after being hit
                        # player.set_texture(1) # This can be used to change image of player after being hit
                        player.width = player.width * 1.5 # increases player size 
                        player.height = player.height * 1.5 # increases player size

                if self.weight >= 400:

                    self.game_over = True
                    self.player_scale = 0.5
                    print("Game over")
                    # pass self, the current view, to preserve this view's state
                    end = End_Menu(self)
                    self.window.show_view(end)
