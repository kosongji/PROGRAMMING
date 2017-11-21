from pico2d import *

class Button:

    def __init__(self,imageFilename,x=0,y=0):
        self.image = load_image(imageFilename)
        self.x,self.y = x,y
       
        

    def draw(self):
        self.image.draw(self.x,self.y)
       
    def ptInRect(self,x,y):
        half_width = self.image.w /2
        if(x < self.x - half_width):
            return False
        if(x>self.x + half_width):
            return False
        half_height = self.image.h /2
        if(y<self.y - half_height):
            return False
        if(y>self.y + half_height):
            return False
        return True
        

    def onOver():
        game_framework.change_state(main_state)


    def handle_event(self,event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            if(self.ptInRect(event.x,600-event.y)):
                self.onOver()



