""" -- game file --

class: game()

functions:  __init__()
            start_new_game()
            create_unhealthy_food()
            create_healthy_food()
            on_draw()
            on_key_press()
            on_key_release()
            on_update()
            
"""
import random
import math
import time
import arcade
import os

from typing import cast
from data import constants
from data.food_sprite import foodsprite
from data.player_sprite import playersprite
from data.pause_menu import pause_menu
from data.end_menu import end_menu
from data.win_menu import win_menu

music_volume = 0.5
class game(arcade.View):
    """ this class is responsible for controling the sequence of play. 
    
    stereotype:
        controller

    attributes: frame_count (integer): in charge of changing the frames of the game.
                player_scale (float): the scale at which the player changes each time food is consumed.
                game_over (boolean): determines whether or not the game should continue.
                player_sprite_list (arcade.spritelist): holds the sprite paths of the player's character.
                healthy_food_list (arcade.spritelist): holds the sprite path of the healthy food(s).
                unhealthy_food_list (arcade.spritelist): holds the sprite path of the unhealthy food(s).
                weight (integer): keeps track of the weight of the character.
                player_sprite (null): initial upload of character sprite.
                left_pressed (boolean): keeps track of left button inputs.
                right_pressed (boolean): keeps track of right button inputs.
                up_pressed (boolean): keeps track of up button inputs.
                down_pressed (boolean): keeps track of down button inputs.
                laser_sound (arcade.load_sound): holds the sprite paths of sounds.
                hit_sound1 (arcade.load_sound): holds the sprite paths of sounds.
                hit_sound2 (arcade.load_sound): holds the sprite paths of sounds.
                hit_sound3 (arcade.load_sound): holds the sprite paths of sounds.
                hit_sound4 (arcade.load_sound): holds the sprite paths of sounds.
    """

    def __init__(self):
        """ the class constructor.
        
        args:
            self (game): an instance of game.
        """
        super().__init__()

        # set the working directory (where we expect to find files) to the same
        # directory this .py file is in. you can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0
        self.player_scale = 0.5
        self.total_time = 0.0
        self.game_over = False

        # sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.healthy_food_list = arcade.SpriteList()
        self.unhealthy_food_list = arcade.SpriteList()

        # set up the player
        self.weight = 250
        self.player_sprite = None

        # track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # sounds
        self.munch = arcade.load_sound(constants.assets_dir / "sounds" / "munch.mp3")
        self.munch2 = arcade.load_sound(constants.assets_dir / "sounds" / "munch2.mp3")
        self.munch3 = arcade.load_sound(constants.assets_dir / "sounds" / "munch3.mp3")
        self.munch4 = arcade.load_sound(constants.assets_dir / "sounds" / "munch4.mp3")
        self.munch5 = arcade.load_sound(constants.assets_dir / "sounds" / "munch5.mp3")

        # music
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
        # self.song = constants.assets_dir / "sounds" / "02 kokiri.mp3"
        self.song = constants.assets_dir / "sounds" / "25_battle of stoicism.mp3"
        
        # set the background color
        arcade.set_background_color(arcade.color.BLACK)


    def play_song(self):

        """ play the song. """
        # stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)

        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(music_volume)
        time.sleep(0.3)

    def on_setup(self):
        self.music_list = [self.song]
        self.current_song_index = 0
        self.play_song()


    def start_new_game(self):
        """ begins the sequence of play.
        
        args:
            self (game): an instance of game.
        """

        self.frame_count = 0
        self.total_time = 0
        self.game_over = False
        self.on_setup()

        arcade.set_background_color(arcade.color.BLACK) 

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.healthy_food_list = arcade.SpriteList()
        self.unhealthy_food_list = arcade.SpriteList()

        # set up the player
        self.weight = 250
        self.player_sprite = playersprite(constants.assets_dir / "images" / "fat-astronaut.png", self.player_scale, self.window.width, self.window.height)
        self.player_sprite_list.append(self.player_sprite)

        # make the unhealthy foods
        if self.window.width > 1300 and self.window.height > 1000:
            starting_food_count = constants.starting_food_count * 2
        elif self.window.width > 2000 and self.window.height > 2000:
            starting_food_count = constants.starting_food_count * 3
        else:
            starting_food_count = constants.starting_food_count
        self.create_unhealthy_food(starting_food_count)

        # make the healthy foods
        self.create_healthy_food(starting_food_count)

    def create_unhealthy_food(self, count):
        """ initializes all sprites for the unhealthy foods.
        
        args:
            self (game): an instance of game.
            count (integer): controls the number of food items present.
        """
        
        image_list = (constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "icecream.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "burger.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "cake.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "candybar.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "cookiechocolate.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "corndog.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "cupcake.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "donutchocolate.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "fries.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "hotdog.png")
        for i in range(count):
            image_no = random.randrange(10)
            food_sprite = foodsprite(image_list[image_no], constants.scale, self.window.width, self.window.height, "bad")
            food_sprite.guid = "food"

            food_sprite.center_y = random.randrange(constants.bottom_limit, self.window.height + constants.offscreen_space)
            food_sprite.center_x = random.randrange(constants.left_limit, self.window.width + constants.offscreen_space)

            food_sprite.change_x = random.random() * 2 - 1 + (self.total_time / 10)
            food_sprite.change_y = random.random() * 2 - 1 + (self.total_time / 10)

            food_sprite.change_angle = (random.random() - 0.5) * 2
            food_sprite.size = 4
            self.unhealthy_food_list.append(food_sprite)

    def create_healthy_food(self, count):
        """ initializes all sprites for the healthy foods.
        
        args:
            self (game): an instance of game.
            count (integer): controls the number of food items present.
            
        """

        image_list = (constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "apple.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "applehalf.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "avocado.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "avocadohalf.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "banana.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "beet.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "broccoli.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "cabbage.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "carrot.png",
                      constants.assets_dir / "images" / "foodkit_v1.2" / "side" / "celerystick.png")
        for i in range(count):
            image_no = random.randrange(10)
            food_sprite = foodsprite(image_list[image_no], constants.scale, self.window.width, self.window.height, "good")
            food_sprite.guid = "food"

            food_sprite.center_y = random.randrange(constants.bottom_limit, self.window.height + constants.offscreen_space)
            food_sprite.center_x = random.randrange(constants.left_limit, self.window.width + constants.offscreen_space)


            food_sprite.change_x = random.random() * 2 * - 1 + (self.total_time / 10) 
            food_sprite.change_y = random.random() * 2 * - 1 + (self.total_time / 10)

            food_sprite.change_angle = (random.random() - 0.5) * 2
            food_sprite.size = 4 

            self.healthy_food_list.append(food_sprite)

        # for i in image_list:
        #     food_sprite.change_x = random.random() * 2 * self.total_time - 1
        #     food_sprite.change_y = random.random() * 2 * self.total_time - 1

        #     food_sprite.change_angle = (random.random() - 0.5) * 2 * self.total_time
        #     food_sprite.size = 4 * self.total_time

    def on_draw(self):
        """ draws each sprite onto the screen.
        
        args:
            self (game): an instance of game.
            
        """

        # this command has to happen before we start drawing
        arcade.start_render()

        # draw all the sprites.
        self.healthy_food_list.draw()
        self.unhealthy_food_list.draw()
        self.player_sprite_list.draw()

        # calculate minutes
        minutes = int(self.total_time) // 60

        # calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60


        # put the text on the screen.
        output = f"weight: {self.weight}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        # output = f"food count: {len(self.healthy_food_list)}"
        output = f"time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)

    def on_key_press(self, symbol, modifiers):
        """ initializes all sprites for the healthy foods.
        
        args:
            self (game): an instance of game.
            symbol (arcade.key): an instance of a key press.
            
        """
        
        if symbol == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = pause_menu(self)
            self.window.show_view(pause)

        if symbol == arcade.key.W:
            self.up_pressed = True
        elif symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.A:
            self.left_pressed = True
        elif symbol == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, symbol, modifiers):
        """ initializes all sprites for the healthy foods.
        
        args:
            self (game): an instance of game.
            symbol (arcade.key): an instance of a key press.
            
        """
        
        if symbol == arcade.key.W:
            self.up_pressed = False
        elif symbol == arcade.key.S:
            self.down_pressed = False
        elif symbol == arcade.key.A:
            self.left_pressed = False
        elif symbol == arcade.key.D:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ move everything """

        self.frame_count += 1
        self.player_sprite.angle += 0.5
        self.total_time += delta_time

        self.move_time = (self.total_time + 1) / 20000

        # increase speed of healthy food over time
        counter = 0
        for food in self.healthy_food_list:
            if counter == 4:
                counter -= 4

            if counter == 0:
                food.change_x += self.move_time
                food.change_y += self.move_time
            elif counter == 1:
                food.change_x -= self.move_time
                food.change_y += self.move_time
            elif counter == 2:
                food.change_x -= self.move_time
                food.change_y -= self.move_time
            elif counter == 3:
                food.change_x += self.move_time
                food.change_y -= self.move_time

            counter += 1

        # increase speed of unhealthy food over time
        counter = 0
        for food in self.unhealthy_food_list:
            if counter == 4:
                counter -= 4

            if counter == 0:
                food.change_x += self.move_time
                food.change_y += self.move_time
            elif counter == 1:
                food.change_x -= self.move_time
                food.change_y += self.move_time
            elif counter == 2:
                food.change_x -= self.move_time
                food.change_y -= self.move_time
            elif counter == 3:
                food.change_x += self.move_time
                food.change_y -= self.move_time

            counter += 1

        # you win if you last for n minutes
        n = 1
        if self.total_time // 60 >= n:
            self.game_over = True
            self.music.stop(self.current_player)
            win = win_menu(self)
            self.window.show_view(win)

        if not self.game_over:
            self.healthy_food_list.update()
            self.unhealthy_food_list.update()
            self.player_sprite_list.update()

            # if not self.player_sprite.respawning:
                            # calculate speed based on the keys pressed
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0


            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = constants.movement_speed
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -constants.movement_speed
            if self.left_pressed and not self.right_pressed:
                self.player_sprite.change_x = -constants.movement_speed
            elif self.right_pressed and not self.left_pressed:
                self.player_sprite.change_x = constants.movement_speed


            # code so the player stays in the same place after being hit and player get's bigger/smaller
            # code works by increasing the player's height and width if they're hit
            self.player_sprite_list.update()
            healthy_foods = arcade.check_for_collision_with_list(self.player_sprite, self.healthy_food_list) 
            if len(healthy_foods) > 0:
                munch_list = [self.munch, self.munch2, self.munch3, self.munch4, self.munch5]
                munch = random.choice(munch_list)
                arcade.play_sound(munch)
                if self.weight > 100:
                    self.weight -= 50
                    constants.movement_speed = constants.movement_speed * 1.5
                    healthy_foods[0].remove_from_sprite_lists()
                    self.create_healthy_food(1)
                    for player in self.player_sprite_list:
                        player.width = player.width / 1.5 # increases player size 
                        player.height = player.height / 1.5 # increases player size
                if self.weight <= 100:
                    constants.movement_speed = 4
                    self.game_over = True
                    self.player_scale = 0.5
                    self.music.stop(self.current_player)
                    print("game over")
                    # pass self, the current view, to preserve this view's state
                    end = end_menu(self)
                    self.window.show_view(end)              

            unhealthy_foods = arcade.check_for_collision_with_list(self.player_sprite, self.unhealthy_food_list) 
            if len(unhealthy_foods) > 0:
                munch_list = [self.munch, self.munch2, self.munch3, self.munch4, self.munch5]
                munch = random.choice(munch_list)
                arcade.play_sound(munch)
                if self.weight > 0:
                    self.weight += 50
                    constants.movement_speed = constants.movement_speed / 1.5
                    unhealthy_foods[0].remove_from_sprite_lists()
                    self.create_unhealthy_food(1)
                    for player in self.player_sprite_list:
                        # player.append_texture(arcade.load_texture(constants.assets_dir + "images/icecream.png")) # this can be used to change image of player after being hit
                        # player.set_texture(1) # this can be used to change image of player after being hit
                        player.width = player.width * 1.5 # increases player size 
                        player.height = player.height * 1.5 # increases player size
                if self.weight >= 400:
                    constants.movement_speed = 4
                    self.game_over = True
                    self.player_scale = 0.5
                    self.music.stop(self.current_player)
                    print("game over")
                    # pass self, the current view, to preserve this view's state
                    end = end_menu(self)
                    self.window.show_view(end)
                
