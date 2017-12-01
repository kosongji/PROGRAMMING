import random
import enemy

from pico2d import *


class Enemy_Bullet:
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


    def __init__(self,x,y):

        self.bx,self.by = x.y
        self.shoot_speed = 1000
        
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('enemy_bullet.png')

            
    def update(self, frame_time):
        self.by -= frame_time * self.shoot_speed
        

  
    def draw(self):
        bx = self.bx
        by = self.by
        self.image.clip_draw(0,0,10,40,bx,by)
    
           
