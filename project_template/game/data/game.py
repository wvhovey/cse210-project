"""
food eater

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.food_smasher
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

        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.lives = 3

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
        arcade.set_background_color(arcade.color.AMAZON)

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = PlayerSprite("../assets/images/man.png", constants.SCALE)
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

        # Make the foods
        image_list = ("../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png",
                      "../assets/images/cake.png")
        for i in range(constants.STARTING_food_COUNT):
            image_no = random.randrange(4)
            food_sprite = FoodSprite(image_list[image_no], constants.SCALE)
            food_sprite.guid = "food"

            food_sprite.center_y = random.randrange(constants.BOTTOM_LIMIT, constants.TOP_LIMIT)
            food_sprite.center_x = random.randrange(constants.LEFT_LIMIT, constants.RIGHT_LIMIT)

            food_sprite.change_x = random.random() * 2 - 1
            food_sprite.change_y = random.random() * 2 - 1

            food_sprite.change_angle = (random.random() - 0.5) * 2
            food_sprite.size = 4
            self.food_list.append(food_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.food_list.draw()
        self.player_life_list.draw()
        self.bullet_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        output = f"food Count: {len(self.food_list)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)



    def on_key_press(self, symbol, modifiers):
        """ Called whenever a key is pressed. """
        # Shoot if the player hit the space bar and we aren't respawning.
        if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
            bullet_sprite = TurningSprite("../assets/images/laserBlue01.png", constants.SCALE)
            bullet_sprite.guid = "Bullet"

            bullet_speed = 13
            bullet_sprite.change_y = \
                math.cos(math.radians(self.player_sprite.angle)) * bullet_speed
            bullet_sprite.change_x = \
                -math.sin(math.radians(self.player_sprite.angle)) \
                * bullet_speed

            bullet_sprite.center_x = self.player_sprite.center_x
            bullet_sprite.center_y = self.player_sprite.center_y
            bullet_sprite.update()

            self.bullet_list.append(bullet_sprite)

            arcade.play_sound(self.laser_sound)
        
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


    def split_food(self, food: FoodSprite):
        """ Split an food into chunks. """
        x = food.center_x
        y = food.center_y
        self.score += 1

        if food.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["../assets/images/cake.png",
                              "../assets/images/cake.png"]

                food_sprite = FoodSprite(image_list[image_no],
                                              constants.SCALE * 1.5)

                food_sprite.center_y = y
                food_sprite.center_x = x

                food_sprite.change_x = random.random() * 2.5 - 1.25
                food_sprite.change_y = random.random() * 2.5 - 1.25

                food_sprite.change_angle = (random.random() - 0.5) * 2
                food_sprite.size = 3

                self.food_list.append(food_sprite)
                self.hit_sound1.play()

        elif food.size == 3:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["../assets/images/cake.png",
                              "../assets/images/cake.png"]

                food_sprite = FoodSprite(image_list[image_no],
                                              constants.SCALE * 1.5)

                food_sprite.center_y = y
                food_sprite.center_x = x

                food_sprite.change_x = random.random() * 3 - 1.5
                food_sprite.change_y = random.random() * 3 - 1.5

                food_sprite.change_angle = (random.random() - 0.5) * 2
                food_sprite.size = 2

                self.food_list.append(food_sprite)
                self.hit_sound2.play()

        elif food.size == 2:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = ["../assets/images/cake.png",
                              "../assets/images/cake.png"]

                food_sprite = FoodSprite(image_list[image_no],
                                              constants.SCALE * 1.5)

                food_sprite.center_y = y
                food_sprite.center_x = x

                food_sprite.change_x = random.random() * 3.5 - 1.75
                food_sprite.change_y = random.random() * 3.5 - 1.75

                food_sprite.change_angle = (random.random() - 0.5) * 2
                food_sprite.size = 1

                self.food_list.append(food_sprite)
                self.hit_sound3.play()

        elif food.size == 1:
            self.hit_sound4.play()

    def on_update(self, x):
        """ Move everything """

        self.frame_count += 1

        if not self.game_over:
            self.food_list.update()
            self.bullet_list.update()
            self.player_sprite_list.update()



            for bullet in self.bullet_list:
                foods = arcade.check_for_collision_with_list(bullet, self.food_list)

                for food in foods:
                    self.split_food(cast(FoodSprite, food))  # expected FoodSprite, got Sprite instead
                    food.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()

                # Remove bullet if it goes off-screen
                size = max(bullet.width, bullet.height)
                if bullet.center_x < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_x > constants.SCREEN_WIDTH + size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y > constants.SCREEN_HEIGHT + size:
                    bullet.remove_from_sprite_lists()

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

            # Call update to move the sprite
            # If using a physics engine, call update player to rely on physics engine
            # for movement, and call physics engine here.
                self.player_sprite_list.update()
                foods = arcade.check_for_collision_with_list(self.player_sprite, self.food_list)
                if len(foods) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_food(cast(FoodSprite, foods[0]))
                        foods[0].remove_from_sprite_lists()
                        self.player_life_list.pop().remove_from_sprite_lists()
                        print("Crash")
                    else:
                        self.game_over = True
                        print("Game over")
                        # pass self, the current view, to preserve this view's state
                        end = End_Menu(self)
                        self.window.show_view(end)


