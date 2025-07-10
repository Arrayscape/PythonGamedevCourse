# This file manages all the game objects like the spaceship (player), the asteroids, and the bullets
####################################################################################################
import random # a built-in module for random choice
from pygame.image import load
from pygame.math import Vector2
from pygame.transform import rotozoom

UP = Vector2(0, -1)


# Function to generate a random velocity speed
def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

# GameObject class
# general template to follow for game objects
class GameObject:
    # Function to initialize a game object
    def __init__(self, position, sprite, velocity):
        # self.position
        # self.sprite
        # self.radius 
        # self.velocity
        pass

    # Function to draw the sprite of the game object at a specific location
    def draw(self, surface): 
        pass

    # Function to move the game object to a new position
    def move(self, surface): 
        pass

    # Function to check if object has collided with another
    def collides_with(self, other_obj):
        # did the two objects collide?
        pass

# Spaceship class
# inherits from GameObject
class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    # Function to create a new Spaceship
    def __init__(self, position, create_bullet_callback):
        # self.create_bullet_callback
        # Make a copy of the original UP vector
        # self.direction

        # create sprite
        # return the sprite with alpha -- allows for transparency

        # call superclass init
        pass

    # Function to rotate spaceship
    def rotate(self, clockwise=True):
        pass

    # Function to increase spaceship's velocity 
    def accelerate(self):
        pass

    # Function to draw the spaceship
    def draw(self, surface):
        pass

    # Function to shoot a bullet
    def shoot(self):
        pass


# Asteroid class
# inherits from GameObject
class Asteroid(GameObject):
    # Function to create a new Asteroid
    def __init__(self, position, create_asteroid_callback, size=3):
        # self.create_asteroid_callback
        # self

        # create scaled sprite

        # call superclass init
        pass

    # Function to split the asteroid
    def split(self):
        pass


# Bullet class
# inherits from GameObject
class Bullet(GameObject):
    # Function to create a new Bullet
    def __init__(self, position, velocity):
        sprite = load(f"assets/bullet.png")
        super().__init__(position, sprite, velocity)

    # Function to move the bullet
    #   override so bullets don't wrap around the screen
    def move(self):
        pass