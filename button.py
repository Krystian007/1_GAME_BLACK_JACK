"""
Moduł ładowania img

"""
import pygame


class Button():
    """Create and Draw Button"""

    def __init__(self, parents, pos_x, pos_y, image_path, scale, rotate=0):

        self.parents = parents
        image = pygame.image.load(image_path)
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
        self.image = pygame.transform.rotate(self.image, rotate)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x - (width * scale)/2, pos_y - ((height * scale)/2))
        self.clicked = False


    def draw(self):
        """
        Draw buton on screan, with get mouse position

        Returns
        -------
        bool
            DESCRIPTION.

        """
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                return True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        # draw button on screen
        self.parents.screen.blit(self.image, (self.rect.x, self.rect.y))
