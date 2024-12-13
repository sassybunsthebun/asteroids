# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main(): 
    pygame.init()
    clock =pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    color = (0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        pygame.display.flip()

        dt = pygame.time.Clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
