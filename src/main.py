import pygame
import constants
import sys
import player 

def main():
    pygame.init()
    #Make sure pygame is really initialised
    if not pygame.get_init():
        print("Pygame not initialised!")
        sys.exit(1)

    #Initialise Screen Settings
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    #Instantiate Player
    player_sprite = player.Player(constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2)
    #Get game clock
    game_clk = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
      
    while True:
        #Check for Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
      
        player_sprite.update(dt)     
      
        screen.fill("black")
        #Draw player sprite
        player_sprite.draw(screen) 
        pygame.display.flip()
        dt = game_clk.tick(60) /1000
       
    
if __name__ == "__main__":
    main()