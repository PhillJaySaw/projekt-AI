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
from decision import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.maze = generate_pathfinder_map()
        self.goals = []
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
        self.crops = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == '0' or tile == 'P':
                    Crop(self, col, row)
                # if tile == 'P':
                #     self.player = Player(self, col, row)
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row, self.maze)
                    break

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
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.draw_grid()
        pg.display.flip()

    def get_mouse_pos_tile(self):
        # get the the position of the mouse, based on the tile grid
        # divide pixel value by tile size
        mousePosTile = [0, 0]
        mousePos = pg.mouse.get_pos()
        mousePosTile[1] = math.floor((mousePos[1] / 32))
        mousePosTile[0] = math.floor((mousePos[0] / 32))
        return mousePosTile

    def create_crop_decission(self):
        # add all crops to the right decision array of the player
        for crop in self.crops:
            decision = dtree(crop)
            # print(dtree(crop))
            if decision == "fertilizer":
                self.player.fertilizer.append(crop)
            elif decision == "harvest":
                self.player.harvest.append(crop)
            elif decision == "water":
                self.player.water.append(crop)
            elif decision == "pest":
                self.player.pest.append(crop)
            elif decision == "harvest":
                self.player.weed.append(crop)

    def next_day(self):
        # moves game to next level, all plant grow and change stats
        for crop in self.crops:
            crop.grow()

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

                # print("start: " + str(start))
                # print("end: " + str(end))

                self.path = astar(self.maze, start, end)

                # values flipped for compatibility with a* algorithm
                # print("generated path: " + str(path))
                # self.path = list(map(lambda t: (t[1], t[0]), self.path))
            if event.type == pg.KEYDOWN:
                # this event start the day and crop harvesting
                if event.key == pg.K_RETURN:
                    self.next_day()
                    self.create_crop_decission()

        # start working on the field, until all work is done
        # this statement is only entered if more work is to be done
        # and there is no current goal
        if not self.player.work_done() and len(self.path) == 0:
            if len(self.player.fertilizer):
                next_crop = self.player.fertilizer.pop(0)
                print("fert crop " + str((next_crop.x, next_crop.y)))
                self.path = astar(
                    self.maze, (self.player.y, self.player.x), (next_crop.y, next_crop.x))
            elif len(self.player.harvest):
                next_crop = self.player.harvest.pop(0)
                print("harv crop " + str((next_crop.x, next_crop.y)))
                self.path = astar(
                    self.maze, (self.player.y, self.player.x), (next_crop.y, next_crop.x))
            elif len(self.player.water):
                next_crop = self.player.water.pop(0)
                print("water crop " + str((next_crop.x, next_crop.y)))
                self.path = astar(
                    self.maze, (self.player.y, self.player.x), (next_crop.y, next_crop.x))
            elif len(self.player.pest):
                next_crop = self.player.pest.pop(0)
                print("pest crop " + str((next_crop.x, next_crop.y)))
                self.path = astar(
                    self.maze, (self.player.y, self.player.x), (next_crop.y, next_crop.x))
            elif len(self.player.weed):
                next_crop = self.player.weed.pop(0)
                print("weed crop " + str((next_crop.x, next_crop.y)))
                self.path = astar(
                    self.maze, (self.player.y, self.player.x), (next_crop.y, next_crop.x))

            # move player according to generated path
        if len(self.path) > 0:
            nextMove = self.path.pop(0)
            # print(str(nextMove) + " " + str((self.player.x, self.player.y)))
            nextMove = numpy.subtract(nextMove, (self.player.x, self.player.y))
            # print(nextMove)
            self.player.move(dx=nextMove[0], dy=nextMove[1])

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


# print(str(numpy.subtract((1, 1), (1, 2))))


# create the game object
g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()
