import pygame as pg
import sys
from pistol import Pistol
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from shotgun import Shotgun
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.current_weapon = 0
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.pistol = Pistol(self)
        self.shotgun = Shotgun(self)
        self.weapon = self.shotgun
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
            self.change_weapon(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
    def change_weapon(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                if self.current_weapon == 0:
                    self.current_weapon = 1
                    self.weapon = self.pistol
                else:
                    self.current_weapon = 0
                    self.weapon = self.shotgun


if __name__ == '__main__':
    game = Game()
    game.run()
