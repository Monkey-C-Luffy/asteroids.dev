from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y):
       super().__init__(x,y,PLAYER_RADIUS)
       self.__rotation = 0 
       self.__shot_timer = 0
    
    def set_shot_timer(self,value):
        if value <=0:
            self.__shot_timer = 0
        else:
            self.__shot_timer = value
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
        
    def __shoot(self):
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.__rotation) * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        #Moving
        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
            self.__rotate(dt)
        if keys[pygame.K_w]:
            self.__move(dt)
        if keys[pygame.K_s]:
            self.__move(-dt)
        
        #Shooting
        if keys[pygame.K_SPACE]:
            if self.__shot_timer > 0:
                return
            self.__shoot()
            self.__shot_timer = PLAYER_SHOOT_COOLDOWN
            
        self.set_shot_timer(self.__shot_timer - dt)
        
    