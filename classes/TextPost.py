import pygame
from Post import Post
from constants import *
from helpers import screen


class TextPost(Post):
    def __init__(self, username, location, description, text, color_text, color_background):
        super().__init__(username, location, description)
        self.text = text
        self.color_text = color_text
        self.color_background = color_background

    def display(self):
        screen.fill(self.color_background, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))

        text_font = pygame.font.Font("ttf.chalkduster.ttf", UI_FONT_SIZE)

        rendered_text = text_font.render(self.text, True, self.color_text)
        text_rect = rendered_text.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))

        if text_rect.width > POST_WIDTH:
            scale_factor = POST_WIDTH / text_rect.width
            new_size = int(UI_FONT_SIZE * scale_factor)
            text_font = pygame.font.Font("ttf.chalkduster.ttf", new_size)
            rendered_text = text_font.render(self.text, True, self.color_text)
            text_rect = rendered_text.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))

        screen.blit(rendered_text, text_rect)

        super().display()