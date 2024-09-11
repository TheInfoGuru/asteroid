import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        new_asteroid_1_velocity = self.velocity.rotate(split_angle)
        new_asteroid_2_velocity = self.velocity.rotate(-split_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_1.velocity = new_asteroid_1_velocity * 1.2
        new_asteroid_2.velocity = new_asteroid_2_velocity * 1.2