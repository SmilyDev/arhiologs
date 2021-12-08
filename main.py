import pygame as pg
import sys, datetime
from objects.solder import *
# import objects.controls as controls
from objects.map import *


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0))
        self.display_size = pg.display.get_surface().get_size()
        self.bg_color = (0, 0, 0)

        self.map = Map(self.screen)
        self.player = Player(self.screen)

    def update(self):
        self.datetime = self.player.events(self.map)
        self.player.moving()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.map.draw(self.player)
        self.player.drow_moving_line()
        self.player.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
