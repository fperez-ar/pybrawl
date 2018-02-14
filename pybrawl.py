import pygame
import Character as game_character
import input_handler as input
import screen_input, helper
from os import listdir

pygame.init()
input.init()

display_dimensions = (1024,1024)
title = 'Welcome to pybrawl'
bg2    = pygame.image.load('bg.jpg')
bg    = pygame.image.load('bg1.png')
char  = game_character.AniCharacter( ('xcf/1.png','xcf/2.png','xcf/3.png') )

#game entities
g_entities = [char]

#### SET UP
game_display = pygame.display
game_surface = pygame.display.set_mode(display_dimensions)
clock        = pygame.time.Clock()

game_display.set_caption(title)

input.on_keydown(pygame.K_ESCAPE, quit)



delta = 0
gdone = False

char.x_speed = 10
char.y_speed = 10

print ('character # assigned keyboard')
func = lambda: char.translate( input.get_axis(0), input.get_axis(1) )
char.add_update_event( func )

#### LOOP
while not gdone:

### Event handling ###
  if len ( pygame.event.get(pygame.QUIT) ) > 0 :
      gdone = True

  input.update( pygame.event.get( (pygame.KEYUP, pygame.KEYDOWN) ), delta)

  game_surface.blit( bg2, (0,0))
  game_surface.blit( bg, (0,0))

  for character in g_entities:
     character.update()
     character.render(game_surface)

  game_display.update()

  delta = clock.tick(60)
####end frame

pygame.quit()
quit()
