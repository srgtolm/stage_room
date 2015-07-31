__author__ = 'srgtolm'

from random import randint
from sys import exit

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
#        print randint(0, len(self.quips)-1)
        print "===================================="
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Zala(Scene):
    def enter(self):
        print "History about ZALA"

class Peshera(Scene):
    def enter(self):
        print "History about PECHERA"
class Sklad(Scene):
    def enter(self):
        print "History about SKLAD"

class Gilishe(Scene):
    def enter(self):
        print "History about GILISHE"

class Sokrovishe(Scene):
    def enter(self):
        print "History about SOKROVISHE"

class HappyEnd(Scene):
    def enter(self):
        print "You won! Good job"

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map
        print "SCENE_MAP", scene_map

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
        'gilishe' : Gilishe(),
        'sokrovishe' : Sokrovishe(),
        'death' : Death(),
        'happyend' : HappyEnd()
    }

    def __init__(self, start_scene):
        print "START SCENE", start_scene
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        print "val is", val
        return val

    def opening_scene(self):
        print self.next_scene(self.start_scene)
        return self.next_scene(self.start_scene)

game_map = Map('death')

#game_map.next_scene('death')
#game_map.next_scene('death')
#game_map.opening_scene()

game = Engine(game_map)
game.play()

