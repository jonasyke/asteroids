# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from circleshape import CircleShape
from constants import *
def main():
    pygame.init()    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    px = SCREEN_WIDTH / 2
    py = SCREEN_HEIGHT / 2
    player = Player(px, py)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
