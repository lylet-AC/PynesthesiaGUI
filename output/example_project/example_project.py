import pygame as pg
import sys
import pickle
from settings import *
from classes import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pg.display.set_caption(DISPLAY_TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1, 1)
        self.load_data()
        self.set_current_map(self.map1_map)

    def load_data(self):
        # load the map data
        self.map3_map = pickle.load(
            open(
                os.path.join(
                    LEVELS_FOLDER,
                    "map3.p"),
                "rb"))
        self.map2_map = pickle.load(
            open(
                os.path.join(
                    LEVELS_FOLDER,
                    "map2.p"),
                "rb"))
        self.map1_map = pickle.load(
            open(
                os.path.join(
                    LEVELS_FOLDER,
                    "map1.p"),
                "rb"))

        # load the image data
        self.floor_img = pg.image.load(
            os.path.join(SPRITE_FOLDER, "floor.png"))
        self.floor_img = pg.transform.scale(
            self.floor_img, (TILE_SIZE, TILE_SIZE))
        self.wall_img = pg.image.load(os.path.join(SPRITE_FOLDER, "wall.png"))
        self.wall_img = pg.transform.scale(
            self.wall_img, (TILE_SIZE, TILE_SIZE))
        self.floor_img = pg.image.load(
            os.path.join(SPRITE_FOLDER, "floor.png"))
        self.floor_img = pg.transform.scale(
            self.floor_img, (TILE_SIZE, TILE_SIZE))
        self.barrel_img = pg.image.load(
            os.path.join(SPRITE_FOLDER, "barrel.png"))
        self.barrel_img = pg.transform.scale(
            self.barrel_img, (TILE_SIZE, TILE_SIZE))
        self.tile_img = pg.image.load(os.path.join(SPRITE_FOLDER, "tile.png"))
        self.tile_img = pg.transform.scale(
            self.tile_img, (TILE_SIZE, TILE_SIZE))
        self.tree_img = pg.image.load(os.path.join(SPRITE_FOLDER, "tree.png"))
        self.tree_img = pg.transform.scale(
            self.tree_img, (TILE_SIZE, TILE_SIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.background_sprites = pg.sprite.Group()

        # logic for drawing tiles from a list of lists
        for col, colors in enumerate(self.current_map):
            for row, color in enumerate(colors):
                # each color will load a specific tile
                if color == (230, 230, 19):
                    floor(self, col, row)
                if color == (0, 0, 0):
                    wall(self, col, row)
                if color == (255, 255, 255):
                    floor(self, col, row)
                if color == (0, 0, 255):
                    barrel(self, col, row)
                if color == (255, 0, 0):
                    tile(self, col, row)
                if color == (0, 255, 0):
                    tree(self, col, row)

    def set_current_map(self, map_data):
        # TODO: use this method to change the current map
        self.current_map = map_data

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(DISPLAY_FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.background_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.background_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        pressed = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


g = Game()
while True:
    g.new()
    g.run()
