import os
os.getcwd()
os.chdir('C:\\Users\\LG\\Desktop\\맵만들기')

import json
import time
import game_framework
from pico2d import *

name = "MainState"

canvasWidth = 480
canvasHeight = 272

class TileBackground:
    def __init__(self,filename,width,height):
        f = open(filename)
        self.map = json.load(f)
        self.x = 0
        self.y = 0
        self.canvasWidth =width
        self.canvasHeight =height
        image_filename = self.map['tilesets'][0]['image']
        self.image = load_image(image_filename)
    def draw(self):
        map_width = self.map['width']
        map_height = self.map['height']
        data = self.map['layers'][0]['data']
        tileset = self.map['tilesets'][0]
        tile_width = tileset['tilewidth']
        tile_height = tileset['tileheight']
        margin = tileset['margin']
        spacing = tileset['spacing']
        columns = tileset['columns']
        dx,dy =0 + tile_width/2, 0 + tile_height/2
        desty =dy
        y=0

        while (desty < self.canvasHeight):
            destx = dx
            x=0
            while (destx < self.canvasWidth):
                index = (map_height-y-1) * map_width + x # draw tile
                tile = data[index] 
                tx = (tile-1) % columns
                ty = (tile-1) // columns
                srcx = margin + tx * (tile_width + spacing)
                srcy = self.image.h - (margin + ty * (tile_height + spacing)-1)
                #(srcx,srcy,tile_width,tile_height)
                #(destx,desty)
                self.image.clip_draw(srcx,srcy,tile_width,tile_height,destx,desty)
                destx += tile_width
                x +=1
                print(x,y,index,tile,srcx,srcy,destx,desty)
            desty += tile_height
            y +=1        

bg = None


def enter():
    global canvasWidth,canvasHeight,bg
    open_canvas(canvasWidth,canvasHeight)
    #boy = Boy()
    bg = TileBackground('map.json',canvasWidth,canvasHeight)
def exit():
    global bg
    close_canvas()
   # global boy, backgound
    del(bg)
    #del(Tilebackgound)
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        #    game_framework.change_state(title_state)
def update():
    pass
  
def draw():
    clear_canvas()
    bg.draw()
    #boy.draw()
    update_canvas()
def pause():
    pass
def resume():
    pass
