import pygame
import Character as game_char

pygame.init()

display_dimensions = (800,600)
title = 'Welcome to pybrawl'

bg       = pygame.image.load('bg.jpg')
#fighter1 = pygame.image.load('fighter1')
char = game_char.Character('fighter1.png')

#### SET UP
pygame.display.set_caption(title)
game_display = pygame.display.set_mode(display_dimensions)
clock        = pygame.time.Clock()


pygame.joystick.init()
joystick_exist = (pygame.joystick.get_count() > 0)

if (joystick_exist):
    id_joy = 1
    stick = pygame.joystick.Joystick(id_joy)
    stick.init()

char.x_speed = 10
char.y_speed = 20

gquit = False

#### LOOP

while not gquit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gquit = True
            #
        #print(event)

    #while
    game_display.blit(bg, (0,0))


    ## Move char entity
    x = stick.get_axis(0)
    y = stick.get_axis(1)
    char.translate(x, y)

    game_display.blit( char.sprite, char.get_pos() )

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
