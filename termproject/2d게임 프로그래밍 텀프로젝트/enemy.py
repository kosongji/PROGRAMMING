import random

from enemy_bullet import Enemy_Bullet as Enemy_Bullet

from character import FreeCharacter as Character

from pico2d import *

e_bullet = []


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
        global e_bullet
        
        self.x,self.y =  random.randint(100, 700), 600
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir = 1
        self.ydir = 0
        self.HP = 100
        self.f_time = 0
        self.death = False
        e_bullet = []
        self.stage2 = 0

        if self.stage2 == 1:
            self.HP = 200
            self.death = False

        if Enemy.image == None:
            Enemy.image = load_image('enemy.png')

    def update(self, frame_time):
        global e_bullet,character
        character = Character()
        distance = Enemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME*frame_time
        self.frame = int(self.total_frames) % 1
        self.f_time += frame_time
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)

        if self.f_time >= 0.5:
            e_bullet += [Enemy_Bullet(self.x,self.y-70)]
            self.f_time = 0

        if self.stage2 ==1:
            if self.f_time >= 0.5:
                e_bullet += [Enemy_Bullet(self.x,self.y-70)]
                self.f_time = 0

       
        if self.HP<=0:
            self.death = True
            
        if self.x>750:
            self.xdir = -1
            self.x = 750
            self.state = self.LEFT_RUN
        elif self.x<50:
            self.xdir = 1
            self.x = 50
            self.state = self. RIGHT_RUN
        for i in e_bullet:
            i.update(frame_time)
            if collide(character,i):
                print("character collision")

        if character.C_HP<=80:
            print("gameover")  
    
    
        
    def draw(self):
        global e_bullet
        sx = self.x 
        sy = self.y

        if self.death == False:
            self.image.clip_draw(self.frame * 100,0,100,100,sx,sy)
            for i in e_bullet:
                i.draw()


        

    def get(self):
        return self.x - 50 ,self.y -50,self.x +50, self.y+50
              
def collide(a,b):
    if a.C_death == False and b.C_death == False:
        left_a, bottom_a, right_a, top_a = a.get()
        left_b, bottom_b, right_b, top_b = b.get()
        
        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False
        a.C_HP -= 10
        b.C_death = True
        return True 
