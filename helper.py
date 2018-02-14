import pygame.font as Font
import pygame.draw as Drawer
import pygame.mouse as Mouse

_white = (255, 255, 255)
_grey = (100,100,100)
_dark_grey = (50,50,50)

_red = (190,0,0)
_green = (0,190,0)

_bright_red = (225,0,0)
_bright_green = (0,225,0)

def show_text(surface, text, x, y, color=(255,255,255) ):
    font = Font.SysFont('Arial', 25)
    txt_surface = font.render(text, False, _white)
    surface.blit(txt_surface, (x, y))

def show_button(surface, text, x=0, y=0, on_down=None):
    pass
def dummy():
    rect = Drawer.rect(surface, _grey, (x-7, y-7, 150, 50))
    show_text(surface, text, x, y)

    if rect.collidepoint( Mouse.get_pos() ) and Mouse.get_pressed()[0] == 1:
        return True

    return False

def show_textless_button(surface, color, x=0, y=0, on_down=None):

    rect = Drawer.rect(surface, color, (x-7, y-7, 150, 50))

    if rect.collidepoint( Mouse.get_pos() ) and Mouse.get_pressed()[0] == 1:
        return True

    return False
