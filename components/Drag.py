import sys
import pygame
from functions import set_songs_volume, set_sounds_volume, get_songs_volume, get_sounds_volume
from functions import size as size_func

class Drag:
    """
    Stepped slider. The pointer snaps to `levels_exclusive - 1` evenly spaced points,
    drawn with a green-to-red gradient. Subclasses persist the value in update_variable().
    """

    def __init__(self, position, size, levels_exclusive, max_value):
        self.rect = pygame.rect.Rect(0, 0, size[0], size[1])
        self.rect.center = position
        self.pointer = pygame.rect.Rect(0, 0, size[0] // 5, size[1] // 5)
        self.pointer.center = position
        self.points = [self.rect.left + size[0] // levels_exclusive * level for level in range(1, levels_exclusive)]
        self.points_rects = []
        point_size = size_func(0.3, 4)
        self.color_step = int(510 / levels_exclusive - 1)
        self.colors = [0, 255, 0]

        for point in self.points:
            point_rect = pygame.rect.Rect(0, 0, point_size[0], point_size[1])
            point_rect.center = (point, position[1])
            self.points_rects.append(point_rect)

        self.max_value = max_value
        self.levels_exclusive = levels_exclusive

    def draw(self, screen):
        pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=5)

        # Fade from green to red: raise red first, then lower green.
        for point in self.points_rects:
            pygame.draw.rect(screen, tuple(self.colors), point, border_radius=1)

            if self.colors[0] + self.color_step <= 255:
                self.colors[0] += self.color_step
            elif self.colors[1] - self.color_step >= 0:
                self.colors[1] -= self.color_step

        self.colors = [0, 255, 0]
        pygame.draw.rect(screen, (250, 100, 0), self.pointer, border_radius=5)

    def check_input(self):
        """Snap the pointer to the point nearest the mouse. Returns True if the value changed."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            self.pointer.center = (mouse_pos[0], self.pointer.center[1])
            distances = [abs(self.pointer.center[0] - point) for point in self.points]
            x_desired = distances.index(min(distances))
            self.pointer.center = (self.points[x_desired], self.pointer.center[1])
            self.update_variable(x_desired)
            return True

    def update_variable(self, level):
        pass

class SongsVolumeDrag(Drag):
    def __init__(self, position, size, levels_exclusive, max_value):
        super().__init__(position, size, levels_exclusive, max_value)
        current_level = int(get_songs_volume() / (1 / (self.levels_exclusive - 1)))
        self.pointer.center = (self.points[current_level], position[1])

    def update_variable(self, level):
        set_songs_volume(self.max_value / (self.levels_exclusive - 1) * level)

class SoundsVolumeDrag(Drag):
    def __init__(self, position, size, levels_exclusive, max_value):
        super().__init__(position, size, levels_exclusive, max_value)
        current_level = int(get_sounds_volume() / (1 / (self.levels_exclusive - 1)))
        self.pointer.center = (self.points[current_level], position[1])

    def update_variable(self, level):
        set_sounds_volume(self.max_value / (self.levels_exclusive - 1) * level)
