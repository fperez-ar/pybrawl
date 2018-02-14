import pygame, helper, time



def show(surface):
  clock = pygame.time.Clock()
  done  = False
  offset_x = 50
  input_method = -1
  joysticks_connected = range(pygame.joystick.get_count())
  #print('please select a joystick...')

  if True:
  #while not done:
    helper.show_text(surface, 'please select a joystick...', 100, 200)
    if helper.show_button(surface, 'Quit', 10, 300):
        quit()

    if helper.show_button(surface, 'keyboard', 10, 50):
        input_method = -1
        done = True

    for joystick in joysticks_connected:
        i = joysticks_connected.index(joystick)
        caption = 'joystick'+str(i)
        if helper.show_button(surface, caption, offset_x*i, 50):
            input_method = i
            done = True



    clock.tick(30)
  return input_method
