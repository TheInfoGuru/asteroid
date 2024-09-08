import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt=dt)

        for item in asteroids:
            if item.check_for_collision(player):
                print("Game Over!"); exit()

        screen.fill(color=BLACK)

        for item in drawable:
            item.draw(screen=screen)
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()