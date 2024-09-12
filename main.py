import pygame
import sys
import os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_objects(updatable, dt):
    for object in updatable:
        object.update(dt)

def draw_objects(drawable, screen):
    screen.fill(SCREEN_COLOR)
    for object in drawable:
        object.draw(screen)
    pygame.display.flip()

def check_for_collisions(asteroids, player, shots, score):
    for asteroid in asteroids:
        if asteroid.check_for_collision(player):
            print("Game Over!")
            pygame.quit()
            sys.exit()
        
        for shot in shots:
            if asteroid.check_for_collision(shot):
                score.score += asteroid.split()
                shot.kill()

def main():
    pygame.init()
    pygame.font.init()
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
    Score.containers = drawable

    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    score = Score(font_size=FONT_SIZE, font_file=SCORE_FONT_PATH, font_color=FONT_COLOR, position=SCORE_POSITION)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        handle_events()
        update_objects(updatable, dt)
        check_for_collisions(asteroids, player, shots, score)
        draw_objects(drawable, screen)

        # limit the framerate to 60 FPS
        dt = game_clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()