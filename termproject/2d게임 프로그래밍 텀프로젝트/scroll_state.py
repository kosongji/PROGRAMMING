from pico2d import *

import game_framework
import title_state


from character import FreeCharacter as Character # import Boy class from boy.py
from background import FixedBackground as Background
from enemy import Enemy as Enemy



name = "scroll_state"

button = None
boy = None
background = None
enemy = None

def create_world():
    global character,background,enemy
   
    character = Character()
    background = Background()
    enemy = Enemy()

    background.set_center_object(character)
    character.set_background(background)



def destroy_world():
    global character, background,enemy
    del(character)
    del(background)
    del(enemy)


    
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
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            character.handle_event(event)
            background.handle_event(event)
            

def update(frame_time):
    character.update(frame_time)
    background.update(frame_time)
    #for enemy in Enemies:
    enemy.update(frame_time)

def draw(frame_time):
    clear_canvas()
    background.draw()
    character.draw()
    #for enemy in Enemies:
    enemy.draw()
    
    update_canvas()




