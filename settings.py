import os

""" Define some directories for later use """
# root directory of the Game
ROOT_FOLDER = os.path.dirname(__file__)

# sprite image folder
SPRITE_FOLDER = os.path.join(ROOT_FOLDER, "sprites")

# input image folder
MAP_INPUT_FOLDER = os.path.join(ROOT_FOLDER, "input")

# output folder for storing the finished product
OUTPUT_FOLDER = os.path.join(ROOT_FOLDER, "output")

# level folder for the new game to load created levels
LEVELS_FOLDER = os.path.join(ROOT_FOLDER, "levels")

# files for later use
SETTINGS_FILE = os.path.join(ROOT_FOLDER, "settings.py")

# test folder
TEST_FOLDER = os.path.join(ROOT_FOLDER, "tests")
TEST_IMAGE = os.path.join(TEST_FOLDER, "testmap.png")

""" Game settings here """
# the width of the game window
DISPLAY_WIDTH = 1024

# the height of the game window
DISPLAY_HEIGHT = 768

# the frames per second the game runs at
DISPLAY_FPS = 45

# the text at the top of the game window
DISPLAY_TITLE = ""

# size of the in game tiles
TILE_SIZE = 32

# speed of the player
PLAYER_SPEED = 4
