import pygame, time

class Animation:

    def __init__(self, images_path):
        sprites_li = []
        for f in images_path:
            image = pygame.image.load(f)
            image.set_alpha(128)
            sprites_li.append( image )

        self.__frames = tuple(sprites_li)
        self.__ani_idx = 0
        self.__anim_max = len (self.__frames)
        self.__ani_speed = 1
        self.__fps = 3
        self.__last = 0

    def __elapsed_fps(self):
        current = time.time()
        if (current - self.__last) > 1/self.__fps:
            self.__last = current
            return True
        return False

    def render(self, surface, pos):
        if self.__elapsed_fps():
            self.__ani_idx += 1
            self.__ani_idx = self.__ani_idx % self.__anim_max
        surface.blit( self.__frames[self.__ani_idx], pos )
