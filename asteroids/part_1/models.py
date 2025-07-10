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
        self.position = Vector2(position)

        self.sprite = sprite

        self.radius = self.sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    # Function to draw the sprite of the game object at a specific location
    def draw(self, surface): 
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    # Function to move the game object to a new position
    def move(self, surface): 
        x, y = self.position + self.velocity
        w, h = surface.get_size()
        return Vector2(x % w, y % h)

    # Function to check if object has collided with another
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius # did the two objects collide?

# Spaceship class
# inherits from GameObject
class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    # Function to create a new Spaceship
    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)

        # create sprite
        loaded_sprite = load(f"assets/spaceship.png")
        # return the sprite with alpha -- allows for transparency
        sprite = loaded_sprite.convert_alpha()

        super().__init__(position, sprite, Vector2(0))

    # Function to rotate spaceship
    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    # Function to increase spaceship's velocity 
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    # Function to draw the spaceship
    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    # Function to shoot a bullet
    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)


# Asteroid class
# inherits from GameObject
class Asteroid(GameObject):
    # Function to create a new Asteroid
    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size

        size_to_scale = {3: 1.0, 2: 0.5, 1: 0.25}
        scale = size_to_scale[size]
        loaded_sprite = load(f"assets/asteroid.png")
        sprite = rotozoom(loaded_sprite, 0, scale)

        super().__init__(position, sprite, get_random_velocity(1, 3))

    # Function to split the asteroid
    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)


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
        self.position = self.position + self.velocity