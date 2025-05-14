import pygame
from constants import *
import sys
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    #Make sure pygame is really initialised
    if not pygame.get_init():
        print("Pygame not initialised!")
        sys.exit(1)

    #Initialise Screen Settings
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #Create Groups
    updatable_grp = pygame.sprite.Group()
    drawable_grp = pygame.sprite.Group()
    asteroids_grp = pygame.sprite.Group()
    shots_grp = pygame.sprite.Group()
    #Add containers to classes before instantiation
    Player.containers = (updatable_grp,drawable_grp)
    Asteroid.containers = (asteroids_grp,updatable_grp,drawable_grp)
    AsteroidField.containers = (updatable_grp)
    Shot.containers = (shots_grp,drawable_grp,updatable_grp)
    #Instantiate Player in middle of screen
    player_sprite = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    #Get game clock
    game_clk = pygame.time.Clock()
    dt = 0
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
      
    while True:
        #Check for Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
      
        updatable_grp.update(dt)     
        #Check if any asteroids collided
        for asteroid in asteroids_grp:
            if asteroid.is_colliding(player_sprite):
                print("Game over!")
                sys.exit(0)
            for shot in shots_grp:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
        #Draw player sprite
        for drawable in drawable_grp:
            drawable.draw(screen)

        pygame.display.flip()
        dt = game_clk.tick(60) /1000
       
    
if __name__ == "__main__":
    main()