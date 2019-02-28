import pygame as pg
from settings import *


class floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class barrel(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.barrel_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class tile(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.tile_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class tree(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.background_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.tree_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
