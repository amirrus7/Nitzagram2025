import pygame
from classes.Post import Post
from constants import *
from helpers import screen

class TextPost(Post):
    def __init__(self, username, location, description, text, color_text, color_background):
        super().__init__(username, location, description)
        self.text = text
        self.color_text = color_text
        self.color_background = color_background

    def display(self):
        # ציור רקע הפוסט עם מסגרת
        pygame.draw.rect(screen, self.color_background, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        pygame.draw.rect(screen, BLACK, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT), 2)  # מסגרת שחורה

        # טעינת פונט (אם קובץ הפונט חסר, השתמש בפונט ברירת מחדל)
        try:
            text_font = pygame.font.Font("ttf.chalkduster.ttf", UI_FONT_SIZE)
        except FileNotFoundError:
            text_font = pygame.font.Font(None, UI_FONT_SIZE)

        # יצירת הטקסט
        rendered_text = text_font.render(self.text, True, self.color_text)
        text_rect = rendered_text.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))

        # אם הטקסט רחב מדי, מתאימים את גודל הפונט
        if text_rect.width > POST_WIDTH - 20:  # השארת מרווח של 20 פיקסלים מהקצוות
            scale_factor = (POST_WIDTH - 20) / text_rect.width
            new_size = max(12, int(UI_FONT_SIZE * scale_factor))  # מגביל גודל מינימלי ל-12 פיקסלים
            text_font = pygame.font.Font(None, new_size)
            rendered_text = text_font.render(self.text, True, self.color_text)
            text_rect = rendered_text.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))

        # הצגת הטקסט
        screen.blit(rendered_text, text_rect)

        # הצגת מידע נוסף (כגון שם המשתמש ומיקום)
        super().display()