import os
os.getcwd()
os.chdir('C:\\Users\\LG\\Desktop\\2d')



import random
import game_framework

from pico2d import *

def enter():
    global boy, grass
    #boy = Boy()
    #grass = Grass()
def exit():
    global boy, grass
    #del(boy)
    #del(grass)
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
def update():
    pass
def draw():
    clear_canvas()
    #grass()
    #boy.draw()
    update_canvas()
def pause():
    pass
def resume():
    pass
