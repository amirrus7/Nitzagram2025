import pygame
from constants import *
from helpers import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost

def main():
    pygame.init()

    # יצירת מסך
    screenn = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # טעינת רקע
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # יצירת פוסטים פעם אחת בלבד
    post1 = ImagePost("Images/ronaldo.jpg", 100, ["Great!", "Nice photo!"])
    post2 = TextPost("Just another text post", 50, ["Interesting!", "I agree."])
    posts = [post1, post2]

    current_post_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # יציאה מהלולאה כשסוגרים את החלון

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # קליק שמאלי
                    current_post_index = (current_post_index + 1) % len(posts)  # מעבר בלולאה

        screenn.fill(BLACK)
        screenn.blit(background, (0, 0))

        # תצוגת הפוסט הנוכחי
        posts[current_post_index].display(screenn)

        pygame.display.update()  # עדכון התצוגה
        clock.tick(60)  # שמירה על קצב התצוגה

    pygame.quit()  # סגירת pygame

if __name__ == "__main__":
    main()