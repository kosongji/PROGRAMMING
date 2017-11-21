import random

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('starBackground.png')
        self.w = self.image.w
        self.h = self.image.h

        self.speed = 500
        self.left = 0
        self.screen_width = 800
        self.screen_height = 600
       

    def set_center_object(self, character):
        self.center_object = character


    def draw(self):
        x = int(self.left)
        self.image.clip_draw_to_origin(0, x,  self.screen_width, self.screen_height, 0, 0)
       

    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.h




    def handle_event(self, event):
        pass



