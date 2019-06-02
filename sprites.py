import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

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

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
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
    def __init__(self, maze):
        self.maze = maze
        self.state = []
        generate_crop_info()

    def generate_crop_info():
        pass


class Crop(pg.sprite.Sprite):
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
        self.plant_level = 0
        self.water_level = 0
        self.weed_level = 0
        self.fert_level = False
        self.pest_level = 0
