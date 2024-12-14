import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #makes the screen the defined screen size
    clock = pygame.time.Clock() #sets the time clock to ensure proper FPS

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #sets the player in the middle of the screen
    dt = 0
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #player.update(dt)
        for object in updatable: 
            object.update(dt)

        for asteroid in asteroids: 
            if asteroid.collides_with(player):
                print("game over!")
                sys.exit()

        screen.fill("black")

        for object in drawable: 
            object.draw(screen)
        #player.draw(screen)
        pygame.display.flip()

        #set the framerate to 60 FPS
        dt = clock.tick(60) / 1000    

if __name__ == "__main__":
    main()
