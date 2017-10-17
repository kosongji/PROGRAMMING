import os
os.getcwd()
os.chdir('C:\\Users\\LG\\Desktop\\2d')

import random

import numbers

from pico2d import *


                
open_canvas()       




class Boy:
    image = None
    run_frames =0 

    LEFT_RUN, RIGHT_RUN,LEFT_STAND,RIGHT_STAND = 0, 1, 2, 3
    
    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x< 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0


    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0





    
    def __init__(self):
        self.x,self.y =  random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.index = 0
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
      
    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100,self.x, self.y)
        numbers.draw(self.index, self.x + 20, self.y - 20, 0.5)
        



    handle_state = {
    LEFT_RUN: handle_left_run,
    RIGHT_RUN: handle_right_run,
    LEFT_STAND: handle_left_stand,
    RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)


team = [Boy() for i in range(1000)]


              
class Grass:
 def __init__(self):
  self.image = load_image('grass.png')
 def draw(self):
  self.image.draw(400,30)

num=0

    
def handle_events():
        global running
        global x, y
        global num
       
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False

            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False    

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    num -= 1
                    print("소년의 번호:",num+1)
                if event.key == SDLK_UP:
                    num += 1
                    print("소년의 번호:",num+1)

               

            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y
                team[num].x,team[num].y = x,y
                for boy in team:
                    team[num].index = num+1
                
            


def main():

    
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()


        
        for boy in team:
            boy.update()

        clear_canvas()
        grass.draw()

        for boy in team:
            boy.draw()   

        numbers.draw(num+1,740,540)

        update_canvas()

        delay(0.05)

    close_canvas()

if __name__ == '__main__':
    main()
            
                 

 

  
