import pygame as pg
from settings import *
from a_star import *


class Player(pg.sprite.Sprite):
    # this is the class for out traktor
    def __init__(self, game, x, y, maze):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.maze = maze

        # attributes for crop decisions
        self.harvest = []
        self.water = []
        self.fertilizer = []
        self.pest = []
        self.weed = []
        self.crop_count = 0

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def move_to_point(self, maze, end):
        # move to a given point, using a*
        path = astar(self.maze, (self.y, self.x), end)
        print(path)

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def print_current_crop(self):
        for crop in self.game.crops:
            if crop.x == self.x and crop.y == self.y:
                return [
                    crop.plant_level,
                    crop.water_level,
                    crop.weed_level,
                    crop.fert_level,
                    crop.pest_level,
                ]
                break

    def get_current_crop(self):
        for crop in self.game.crops:
            if crop.x == self.x and crop.y == self.y:
                return crop
                break

    def work(self):
        for crop in self.fertilizer:
            crop_position = (crop.y, crop.x)
            self.move_to_point(self.maze, crop_position)

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
    # class for obstacles, like walls
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Field():
    # this class is propably useless
    def __init__(self, maze):
        self.maze = maze
        self.state = []
        generate_crop_info()

    def generate_crop_info():
        pass


class Crop(pg.sprite.Sprite):
    # class for crops
    def __init__(self, game, x, y):
        # pygame attributes
        self.groups = game.all_sprites, game.crops
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        # crop attributes
        self.plant_level = 3
        self.water_level = 1
        self.weed_level = 1
        self.fert_level = 0
        self.pest_level = 1

    def __str__(self):
        return str([
            self.plant_level,
            self.water_level,
            self.weed_level,
            self.fert_level,
            self.pest_level
        ])

    def get_crop_values(self):
        return [
            self.plant_level,
            self.water_level,
            self.weed_level,
            self.fert_level,
            self.pest_level
        ]

    def grow(self):
        self.plant_level += 1
        self.water_level += 1
        self.weed_level += 1
