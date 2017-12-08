import random
import character 
from pico2d import *

class Bullet:
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

        self.bx,self.by = x,y
        self.shoot_speed = 1000
        self.death = False
        #self.frame = random.randint(0, 7)
        
        if Bullet.image == None:
            Bullet.image = load_image('bullet.png')
            
    def update(self, frame_time):
        self.by += frame_time * self.shoot_speed
        

    def draw(self):
        bx = self.bx
        by = self.by
        #self.image.clip_draw(self.frame * 100,0,10,50,bx,by)
        if self.death == False:
            self.image.clip_draw(0,0,10,50,bx,by)
    def get(self):
        return self.bx -5,self.by - 5,self.bx+5,self.by+5
           
