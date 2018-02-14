import pygame

x_axis = 0
y_axis = 0

x_accel = 0.03
y_accel = 0.03

__k_events = { }
__joysticks = []

__up_dir_keys    = [pygame.K_UP, pygame.K_w]
__down_dir_keys  = [pygame.K_DOWN, pygame.K_s]
__right_dir_keys = [pygame.K_RIGHT, pygame.K_d]
__left_dir_keys  = [pygame.K_LEFT, pygame.K_a]

#TODO: add optional Config for fwd/bwd movement

def init():
    global __joysticks
    __joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    for stick in __joysticks:
        stick.init();

    print ('found', pygame.joystick.get_count(),' joysticks')
    #TODO: implement joystick selection?

def on_keydown(key, ev):
    __k_events[key] = ev


def get_joystick(joystick_id = 0):
  return pygame.joystick.Joystick(joystick_id)

def get_joystick_count():
    return pygame.joystick.get_count();

def joystick_exist():
    return get_joystick_count() > 0

def get_horizontal(event):
    global x_axis

    if event.type == pygame.KEYUP:
        if event.key in __right_dir_keys or event.key in __left_dir_keys:
            x_axis = 0
    elif event.type == pygame.KEYDOWN:
        if event.key in __right_dir_keys:
            x_axis = 1
        elif event.key in __left_dir_keys:
            x_axis = -1

    return x_axis

def get_vertical(event):
    global y_axis

    if event.type == pygame.KEYUP:

        if event.key in __up_dir_keys or event.key in __down_dir_keys:
            y_axis = 0
    elif event.type == pygame.KEYDOWN:
        if event.key in __up_dir_keys:
            y_axis = -1
        elif event.key in __down_dir_keys:
            y_axis = 1

    return y_axis

def get_axis(axis):
        if axis == 0:
            return x_axis
        elif axis == 1:
            return y_axis

def get_joystick_axis(axis, joystick_id=0):
        return get_joystick(joystick_id).get_axis(axis)

def update(events, delta):

    global x_accel, y_accel
    global __k_events

    for event in events:

        get_vertical(event)
        get_horizontal(event)

        if event.type == pygame.KEYDOWN:
         #if event.key in __k_events.keys():
            for keys in __k_events:
              if event.key == keys:
                  __k_events[keys]()


"""
if input.get_joystick_count() > 0 :
    for c in g_entities:
        joy_id = -1
        while joy_id < 0:
            joy_id = screen_input.show(game_surface)

        if joy_id > -1:
            print ('character #', joy_id, 'assigned joystick', joy_id)
            func = lambda: c.translate( input.get_axis(0, joy_id ), input.get_axis(1, joy_id ))
            c.add_update_event( func )
        else:
            print ('character # assigned keyboard')
            func = lambda : c.translate( input.get_axis(0), input.get_axis(1) )
            c.add_update_event( func )
"""
