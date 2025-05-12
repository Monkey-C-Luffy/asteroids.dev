import pygame
import constants
import sys

def main():
    pygame.init()
    #Make sure pygame is really initialised
    if not pygame.get_init():
        print("Pygame not initialised!")
        sys.exit(1)
        return
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    
if __name__ == "__main__":
    main()