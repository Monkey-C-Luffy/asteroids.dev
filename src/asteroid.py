from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"red",self.position,self.radius,2)
        
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #if asteroid is min,give max score
            print(f"Asteroid with radius:{self.radius} has been destroyed,MAX score given:{ASTEROID_PTS_MAX_SCORE}")
            return ASTEROID_PTS_MAX_SCORE

        angle = random.uniform(20,50)
        split_vector_L = self.velocity.rotate(angle)
        split_vector_R = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_L = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_R = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_L.velocity = split_vector_L * 1.2
        asteroid_R.velocity = split_vector_R * 1.2
        
        score = self.calculate_score() 
        print(f"Asteroid with radius:{self.radius} has been split, score given:{score}")
        return score
    
    def calculate_score(self):
        return (ASTEROID_MAX_RADIUS - self.radius+4) * ASTEROID_PTS_MULT