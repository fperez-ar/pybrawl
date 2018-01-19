import pygame

class Character:
    x = 0
    y = 0
    x_speed = 1
    y_speed = 1

    sprite = ''

    def __init__(self, image_path):
        self.sprite = pygame.image.load(image_path)

    def get_pos(self):
        return (self.x, self.y)

    def set_pos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def translate(self, xadd, yadd):
        self.x += xadd * self.x_speed
        self.y += yadd * self.y_speed

    def update(self):
        pass
