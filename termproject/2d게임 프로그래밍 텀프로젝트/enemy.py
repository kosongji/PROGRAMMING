import random

from pico2d import *

class Enemy:
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

    LEFT_RUN, RIGHT_RUN = 0,1

    def __init__(self):
        self.x,self.y =  random.randint(100, 700), 600
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 1
        self.ydir = 0
        

        if Enemy.image == None:
            Enemy.image = load_image('enemy.png')
    def update(self, frame_time):
        distance = Enemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME*frame_time
        self.frame = int(self.total_frames) % 1
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)
        
        if self.x>750:
            self.xdir = -1
            self.x = 750
            self.state = self.LEFT_RUN
        elif self.x<50:
            self.xdir = 1
            self.x = 50
            self.state = self. RIGHT_RUN
        
   
        
    def draw(self):
        sx = self.x 
        sy = self.y
        self.image.clip_draw(self.frame * 100,0,100,100,sx,sy)
        
    
#Enemies = [Enemy() for i in range(10)]


