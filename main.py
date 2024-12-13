import pygame
from constants import *
from player import Player

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #makes the screen the defined screen size
    clock = pygame.time.Clock() #sets the time clock to ensure proper FPS
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #sets the player in the middle of the screen
    dt = 0
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000    

if __name__ == "__main__":
    main()
