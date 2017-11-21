from pico2d import *

import game_framework
import title_state

from character import FreeCharacter as Character # import Boy class from boy.py
from background import FixedBackground as Background



name = "scroll_state"

button = None
boy = None
background = None

def create_world():
    global character,character,background
   
    character = Character()
    background = Background()

    background.set_center_object(character)
    character.set_background(background)



def destroy_world():
    global character, background
    del(character)
    del(background)


    
def enter():
    #open_canvas(800, 600)
    #hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    #close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDL_QUIT):
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            character.handle_event(event)
            background.handle_event(event)
            

def update(frame_time):
    character.update(frame_time)
    background.update(frame_time)

def draw(frame_time):
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()




