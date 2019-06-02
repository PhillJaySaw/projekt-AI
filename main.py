# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 1
# Project setup
# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
import sys
import math
import time
import numpy
from settings import *
from sprites import *
from a_star import *
from generate_pathfinder_map import *
from os import path


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.maze = generate_pathfinder_map()
        self.path = []

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 100
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def get_mouse_pos_tile(self):
        # get the the position of the mouse, based on the tile grid
        # divide pixel value by tile size
        mousePosTile = [0, 0]
        mousePos = pg.mouse.get_pos()
        mousePosTile[1] = math.floor((mousePos[1] / 32))
        mousePosTile[0] = math.floor((mousePos[0] / 32))
        return mousePosTile

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # select dest for player
                # use pathfinder
                pos = self.get_mouse_pos_tile()

                # values flipped for compatibility with a* algorithm
                start = (self.player.y, self.player.x)
                end = (pos[1], pos[0])

                print("start: " + str(start))
                print("end: " + str(end))

                self.path = astar(self.maze, start, end)

                # values flipped for compatibility with a* algorithm
                print("generated path: " + str(path))
                self.path = list(map(lambda t: (t[1], t[0]), self.path))

        # move player according to generated path
        if len(self.path) > 0:
            nextMove = self.path.pop(0)
            print(str(nextMove) + " " + str((self.player.x, self.player.y)))
            nextMove = numpy.subtract(nextMove, (self.player.x, self.player.y))
            print(nextMove)
            self.player.move(dx=nextMove[0], dy=nextMove[1])

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


print(str(numpy.subtract((1, 1), (1, 2))))


# create the game object
g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()
