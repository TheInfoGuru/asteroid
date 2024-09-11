import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, shots, drawable)
    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt=dt)

        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game Over!"); sys.exit()

            for shot in shots:
                if asteroid.check_for_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill(color=BLACK)

        for object in drawable:
            object.draw(screen=screen)
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()