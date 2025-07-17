# This file manages the game itself
####################################################################################################
import pygame # the main module for python game dev
from pygame.image import load
from pygame.math import Vector2

from models import GameObject, Spaceship, Bullet, Asteroid # import the GameObject class from models.py

# GAME CLASS ###################################################################################################
class AsteroidsGame:
    MIN_ASTEROID_DISTANCE = 250

    # Function to start a new Asteroids game
    def __init__(self):
        # start up pygame
        pygame.init()
        pygame.display.set_caption("Asteroids by Arrayscape")
        # set display and initialize variables
        self.screen = pygame.display.set_mode((800, 600)) # create a display
        self.background = load("assets/space.png") # set the background

        # additional game objects and variables
        # clock
        # list of asteroids
        # list of bullets
        # spaceship
        # message font object
        # game over message

        # TODO

    # Function to handle input
    def handle_input(self):
        # loop events
            # quit pygame
        # TODO
        pass

    # Function to process the game logic
    def process_game_logic(self):
        # TODO
        pass

    # Function to draw the sprites
    def draw_sprites(self):
        # TODO
        # draw background
        
        # draw spaceship

        # draw asteroids

        # draw bullets

        # update
        pass


# MAIN CODE ###################################################################################################
# start up pygame
new_asteroids_game = AsteroidsGame()

# run the game -- this is our game loop!
while True:
    new_asteroids_game.handle_input() # handle any user input
    new_asteroids_game.process_game_logic() # process the logic behind the game
    new_asteroids_game.draw_sprites() # draw the sprites and output