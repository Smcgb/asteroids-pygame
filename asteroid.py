import pygame
from constants import *
from circleshape import CircleShape
import random
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        split_1_velocity = self.velocity.rotate(split_angle)
        split_2_velocity = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_1.velocity = split_1_velocity * 1.2

        
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2.velocity = split_2_velocity * 1.2
        

    
