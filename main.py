# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from circleshape import CircleShape
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()

    AsteroidField.containers = (asteroidfield, updateable)

    Asteroid.containers = (asteroids, updateable, drawable)

    Player.containers = (updateable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for ast in asteroids :
            if ast.collision(player):
                print("Game over!")
                return

        screen.fill("black")
    
        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
