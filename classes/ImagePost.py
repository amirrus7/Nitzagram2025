import pygame
from classes.Post import Post
from constants import *
from helpers import screen  # לוודא שה-screen מוגדר

class ImagePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)

        # ניסיון לטעון תמונה, עם טיפול בשגיאה אם היא חסרה
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))
        except pygame.error:
            print(f"Error: Unable to load image {image_path}")
            self.image = None  # במקרה של שגיאה, נמנע מקריסה

    def display(self):
        if screen is None:
            print("Error: screen is not initialized")
            return

        if self.image:  # אם התמונה נטענה בהצלחה
            screen.blit(self.image, (POST_X_POS, POST_Y_POS))

        # ציור מסגרת שחורה סביב התמונה
        pygame.draw.rect(screen, BLACK, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT), 2)

        # הצגת שם משתמש, מיקום ותיאור
        super().display()