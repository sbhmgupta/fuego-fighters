import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, type):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load sprites for the plane
        sprite_sheet = pygame.image.load(
            'resources/' + type['spritesheet_filename']
        ).convert_alpha()

        self.width = type['width']
        self.height = type['height']

        # extract images
        self.images = []
        for i in range(type['rows']):
            for j in range(type['columns']):
                # Rect(left, top, width, height)
                rect = pygame.Rect((j * self.width, i * self.height,
                                    self.width, self.height))
                image = pygame.Surface(rect.size).convert()
                image.set_colorkey(image.get_at((0, 0)), pygame.RLEACCEL)
                image.blit(sprite_sheet, (0, 0), rect)
                self.images.append(image)

        self.rect = self.images[0].get_rect()
