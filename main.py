import pygame
from helpers import *


def main():
    pygame.init()

    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = ImagePost("Images/post1.jpg", 100, ["Great!", "Nice photo!"])
    post2 = TextPost("Just another text post", 50, ["Interesting!", "I agree."])
    posts = [post1, post2]

    current_post_index = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # בדיקה אם זה קליק שמאלי
                    current_post_index += 1
                    if current_post_index >= len(posts):
                        current_post_index = 0  # חזרה לפוסט הראשון אם הגעת לסוף

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        posts[current_post_index].display(screen)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()