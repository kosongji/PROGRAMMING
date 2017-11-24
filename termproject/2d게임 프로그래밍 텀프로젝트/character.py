import random

import bullet

from pico2d import *


class FreeCharacter:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 80.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None


    def __init__(self):
        self.x, self.y = 400,55
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 0
        self.ydir = 0

        if FreeCharacter.image == None:
            FreeCharacter.image = load_image('player.png')


    def set_background(self, bg):
        self.bg = bg

    def update(self, frame_time):
        distance = FreeCharacter.RUN_SPEED_PPS * frame_time
        self.total_frames += FreeCharacter.FRAMES_PER_ACTION * FreeCharacter.ACTION_PER_TIME*frame_time
        self.frame = int(self.total_frames) % 1
        self.x += (self.xdir * distance) 
        self.y += (self.ydir * distance)
        if self.x< 50:
            self.x = 50
        elif self.x > 750:
            self.x = 750
        elif self.y >600:
            self.y = 600
        elif self.y < 50:
            self.y = 50


    def draw(self):
        sx = self.x 
        sy = self.y
        self.image.clip_draw(self.frame * 100,0,100,100,sx,sy)
        debug_print('x=%d, y=%d, sx=%d, sy=%d' % (self.x,self.y,sx,sy))
       
        

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT: self.xdir += 1
            elif event.key == SDLK_UP: self.ydir += 1
            elif event.key == SDLK_DOWN: self.ydir -= 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            elif event.key == SDLK_UP: self.ydir -= 1
            elif event.key == SDLK_DOWN: self.ydir += 1

       # if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            
