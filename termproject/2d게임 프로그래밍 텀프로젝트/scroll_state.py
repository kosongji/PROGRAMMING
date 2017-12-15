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
bgm = None


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
    global bsound,bgm
    #open_canvas(800, 600)
    #hide_cursor()
    game_framework.reset_time()
    create_world()

    if bsound == None:
        bsound = load_wav('bullet_sound.wav')
        bsound.set_volume(32)
   # if bgm == None:
       # bgm = load_wav('bgm.wav')
       #bgm.set_volume(32)
        #bgm.repeat_play()
            


def exit():
    destroy_world()
    #close_canvas()


def pause():
    pass

def resume():
    pass


def collide(a,b):
    if a.death == False and b.death == False:
        left_a, bottom_a, right_a, top_a = a.get()
        left_b, bottom_b, right_b, top_b = b.get()

        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False
        a.HP -= 10
        b.death = True
        return True

              

def handle_events(frame_time):
    global bullet,bsound,bgm
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
       
            
                
            
            

def update(frame_time):
    global bullet,bgm
    
   
    background.update(frame_time)
    if enemy.death == False:
        enemy.update(frame_time)
    
    if character.C_death == False:
        character.update(frame_time)
    for i in bullet:
        i.update(frame_time)


    for b in bullet:
        if collide(enemy,b):
            print("collision")

def draw(frame_time):
    global bullet
    clear_canvas()
    background.draw()
    if character.C_death == False:
        character.draw()
    enemy.draw()

    for i in bullet:
        i.draw()


    
    update_canvas()




