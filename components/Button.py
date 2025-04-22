import pygame

class Button:
    """Clickable button showing either text or an image, with an optional hover colour."""

    def __init__(self, position:tuple, size:tuple, radius=0, text=None, font=None, image=None, background_color=None, hover_color=None):
        self.rect = pygame.rect.Rect(0, 0, size[0], size[1])
        self.rect.center = position

        if font:
            self.text = font.render(text, True, (0, 0, 0))
        self.image = image
        if self.image:
            self.image_rect = self.image.get_rect()
            self.image_rect.center = position

        self.background_color = background_color
        self.hover_color = hover_color
        self.radius = radius

        self.checked = False  # True while the mouse is over the button

    def draw(self, screen):
        if self.image:
            if self.background_color and not self.checked:
                pygame.draw.rect(screen, self.background_color, self.rect, border_radius=10)
            elif self.hover_color and self.checked:
                pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=10)
            screen.blit(self.image, self.image_rect)
        else:
            background_color = self.hover_color if self.checked else self.background_color
            pygame.draw.rect(screen, background_color, self.rect, border_radius=self.radius)
            text_rect = self.text.get_rect(center=self.rect.center)
            screen.blit(self.text, text_rect)

    def check_input(self):
        """Update the hover state and return True if the button is being clicked."""
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self.checked = self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

        return self.checked and mouse_buttons[0]
