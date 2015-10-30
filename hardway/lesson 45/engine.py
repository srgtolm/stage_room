__author__ = 'srgtolm'


'Basic imports'
from random import randint
from sys import exit

'______________________'

'Import modules of game'
from room_zala import Zala
from room_peshera import  *
from room_happyend import *
from room_sklad import *
from room_basement import *
from room_traktir import *
from room_other import *
from stats import *

'______________________'

'Code starts here'


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map
        #print "SCENE_MAP", scene_map

#    def param(self):


    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('happyend')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Map(object):
    scenes = {
        'zala' : Zala(),
        'peshera' : Peshera(),
        'sklad' : Sklad(),
        'basement' : Basement(),
        'traktir' : Traktir(),
        'sokrovishe' : Sokrovishe(),
        'death' : Death(),
        'happyend' : Happyend()
    }

    def __init__(self, start_scene):
        #print "START SCENE", start_scene
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        #print "val is", val
        return val

    def opening_scene(self):
        #print self.next_scene(self.start_scene)2
        return self.next_scene(self.start_scene)

game_map = Map('zala')
game_engine = Engine(game_map)

game_engine.play()



