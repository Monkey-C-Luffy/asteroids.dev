from circleshape import *
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
       super().__init__(x,y,PLAYER_RADIUS)
       self.__rotation = 0 
       # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        
    def __rotate(self,dt):
        self.__rotation += PLAYER_TURN_SPEED * dt    
    
    def __move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
            self.__rotate(dt)
        if keys[pygame.K_w]:
            self.__move(dt)
        if keys[pygame.K_s]:
            self.__move(-dt)
    