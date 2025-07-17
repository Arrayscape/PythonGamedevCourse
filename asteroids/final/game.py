# This file manages the game itself
####################################################################################################
import random # a built-in module for random choice
import pygame # the main module for python game dev
from pygame import Color
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
        self.clock = pygame.time.Clock()
        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400,300), self.bullets.append) # create a new spaceship (player)
        self.font = pygame.font.Font(None, 64)
        self.message = ""

        # generate initial asteroids
        for _ in range(5):
            while True:
                position = Vector2(
                random.randrange(self.screen.get_width()),
                random.randrange(self.screen.get_height()),
            )
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))

    # Function to handle input
    def handle_input(self):
        for event in pygame.event.get():
            # quit pygame
            if event.type == pygame.QUIT:
                pygame.quit()
            # spaceship shooting
            if (self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
            
        # spaceship movement
        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship: # spaceship must exist before we do anything!
            # rotating spaceship
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            # moving spaceship forward
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()


    # Function to process the game logic
    def process_game_logic(self):
        # processing spaceship
        if self.spaceship:
            self.spaceship.move(self.screen)
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.message = "You lost!"
                    break
        
        # processing asteroids
        for asteroid in self.asteroids[:]:
            asteroid.move(self.screen)
            
        # processing collision
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                # if any collision
                if asteroid.collides_with(bullet):
                    # destroy the two collided objects
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    # and split asteroid
                    asteroid.split()
                    break

        # processing bullets
        for bullet in self.bullets[:]:
            bullet.move()
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        # all asteroids destroyed and player is still alive 
        if not self.asteroids and self.spaceship:
            self.message = "You win!"

    # Function to draw the sprites
    def draw_sprites(self):
        # draw background
        self.screen.blit(self.background, (0,0))

        # draw spaceship
        if self.spaceship:
            self.spaceship.draw(self.screen)

        # draw asteroids
        for game_object in self.asteroids:
            game_object.draw(self.screen)

        # draw bullets
        for game_object in self.bullets:
            game_object.draw(self.screen)

        # draw message
        if self.message:
            text_surface = self.font.render(self.message, False, Color("red"))
            rect = text_surface.get_rect()
            rect.center = Vector2(self.screen.get_size()) / 2
            self.screen.blit(text_surface, rect)

        # update
        pygame.display.flip()
        self.clock.tick(60)



# MAIN CODE ###################################################################################################
# start up pygame
new_asteroids_game = AsteroidsGame()

# run the game -- this is our game loop!
while True:
    new_asteroids_game.handle_input() # handle any user input
    new_asteroids_game.process_game_logic() # process the logic behind the game
    new_asteroids_game.draw_sprites() # draw the sprites and output