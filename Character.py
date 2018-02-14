import pygame
import Animation as anim
class Character:
    x = 0
    y = 0
    x_speed = 1
    y_speed = 1
    sprite = ''
    update_evs = []

    ## Receives image path
    def __init__(self, image):
        self.sprite = pygame.image.load(image)
        self.x = 0
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.update_evs = []

    def get_pos(self):
        return (self.x, self.y)

    def set_pos(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def translate(self, xadd, yadd):
        #print(xadd,' - ', yadd)
        self.x += xadd * self.x_speed
        self.y += yadd * self.y_speed

    def add_update_event(self, ev):
        self.update_evs.append(ev)

    def remove_update_event(self, ev):
        self.update_evs.remove(ev)

    def update(self):
        for ev in self.update_evs:
            ev()

    def render(self, surface):
        surface.blit( self.sprite, get_pos())

class AniCharacter(Character):

    __animation = None

    #Receives tuple or list of character
    def __init__(self, images):
        self.__animation = anim.Animation(images)

    def render(self, surface):
        self.__animation.render(surface, self.get_pos())
