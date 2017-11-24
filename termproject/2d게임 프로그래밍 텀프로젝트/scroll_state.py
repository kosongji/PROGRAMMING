from pico2d import *

import game_framework
import title_state



from character import FreeCharacter as Character # import Boy class from boy.py
from background import FixedBackground as Background
from enemy import Enemy as Enemy
from bullet import Bullet as Bullet


name = "scroll_state"

button = None
boy = None
background = None
enemy = None
bullet = []
bsound = None



def create_world():
    global character,background,enemy,bullet
    character = Character()
    background = Background()
    enemy = Enemy()
    bullet= []
    

    background.set_center_object(character)
    character.set_background(background)



def destroy_world():
    global character, background,enemy,bullet
    del(character)
    del(background)
    del(enemy)
    del(bullet)
    

    
def enter():
    global bsound
    
    #open_canvas(800, 600)
    #hide_cursor()
    game_framework.reset_time()
    create_world()

    if bsound == None:
        bsound = load_wav('bullet_sound.wav')
        bsound.set_volume(32)


def exit():
    destroy_world()
    #close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    global bullet,bsound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:    
                bullet += [Bullet(character.x,character.y+70)]
                bsound.play()
    
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            character.handle_event(event)
            background.handle_event(event)
            #bullet.handle_event(event)
            

def update(frame_time):
    global bullet
    character.update(frame_time)
    background.update(frame_time)
    #for enemy in Enemies:
    for i in bullet:
        i.update(frame_time)
    enemy.update(frame_time)

def draw(frame_time):
    global bullet
    clear_canvas()
    background.draw()
    character.draw()
    #for enemy in Enemies:
    enemy.draw()
    for i in bullet:
        i.draw()
    
    
    update_canvas()




