import pygame
from py.buttons import buttons

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.button_in_mouse(mouse_pos):
                    button.action()

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()