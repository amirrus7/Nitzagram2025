import pygame
class Button:
    def __init__(self, x_pos, y_pos, width, height, action=None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.action = action

    def button_in_mouse(self, mouse_pos):
        x, y = mouse_pos
        return self.x_pos <= x <= self.x_pos + self.width and self.y_pos <= y <= self.y_pos + self.height

    def click(self):
        if self.action:
            self.action()

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
            for button in button:
                if button.button_in_mouse(mouse_pos):
                    button.click()

    for button in button:
        pygame.draw.rect(screen, (0, 0, 255), (button.x_pos, button.y_pos, button.width, button.height))

    pygame.display.flip()

pygame.quit()