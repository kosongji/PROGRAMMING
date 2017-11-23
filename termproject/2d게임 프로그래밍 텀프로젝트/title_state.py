
import random

from pico2d import *


import scroll_state as main_state
import game_framework
import uif



name = "TitleState"
image = None
def enter():
    global image,button
    image = load_image('Shooting_Stars.png')
    button = uif.Button('gamestart.png',200,100)
    button.onOver = onBtn
def exit():
    global image
    del(image)
def handle_events(frame_time):
    global button
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            button.handle_event(event)
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def onBtn():
    game_framework.change_state(main_state)
    
def draw(frame_time):
    global button
    clear_canvas()
    image.draw(400, 325)
    button.draw()
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass
def resume():
    pass    
