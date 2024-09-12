import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self, font_size: int, font_file: str, font_color: str, position: tuple):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = position
        self.font = pygame.font.Font(None, font_size)
        self.font_color = font_color
        self.score = 0

    def get_score_text(self):
        return self.font.render(f'Score {self.score}', True, self.font_color)

    def draw(self, screen):
        screen.blit(self.get_score_text(), self.position)