import os
from shutil import copy2, copytree
import pickle
# local imports
from settings import *
import utilities


def create_new_game():

    GAME_TITLE = input("[newgame] Please enter a name for your project: ")

    # define some directories
    NEW_GAME_FOLDER = os.path.join(OUTPUT_FOLDER, GAME_TITLE)
    LEVELS_FOLDER = os.path.join(NEW_GAME_FOLDER, "levels")

    # get the input image with this prompt for the user
    prompt = "\n[newgame] Please enter an image for the map: "
    input_image = utilities.get_image_if_valid(prompt, MAP_INPUT_FOLDER)

    # the map file will be named this
    DEFAULT_MAP_TITLE = input(
        "[newgame] Please enter a title for your new map: ")

    # gather the list of unique colors from the input image
    unique_color_list = utilities.get_unique_color_list(input_image)

    # use the unique color list to generate the color dictionary
    color_dict = utilities.get_color_dict(unique_color_list)

    # try to make directories, copy files, and write data
    try:
        os.mkdir(NEW_GAME_FOLDER)
        os.mkdir(LEVELS_FOLDER)
        copy_necessary_files(NEW_GAME_FOLDER)
        create_map(LEVELS_FOLDER, input_image, DEFAULT_MAP_TITLE)
        create_pygame_classes(GAME_TITLE, NEW_GAME_FOLDER, color_dict)
        create_main_game_code(
            GAME_TITLE,
            NEW_GAME_FOLDER,
            color_dict,
            DEFAULT_MAP_TITLE)
        set_unique_colors_list(LEVELS_FOLDER, unique_color_list)

    # if we encounter an exception print a failure message.
    except BaseException as e:
        print("[newgame] Creation of the new game at: \n{} has failed".format(
            NEW_GAME_FOLDER))
        print(e)

    # if we did not encounter an error, print that it was successfully created
    else:
        print("[newgame] Successfully created the new game at:\n{} ".format(
            NEW_GAME_FOLDER))


def copy_necessary_files(NEW_GAME_FOLDER):
    """This method will copy important files to the new game directory"""

    # copy settings.py to the new game folder
    copy2(SETTINGS_FILE, NEW_GAME_FOLDER)
    # copy the everything in our current SPRITE_FOLDER to a new sprites
    # directory in the new game
    copytree(SPRITE_FOLDER, os.path.join(NEW_GAME_FOLDER, "sprites"))


def set_unique_colors_list(LEVELS_FOLDER, unique_color_list):
    """This method will dump the unique colors list into the levels directory of a game"""

    # place this list into the levels folder of an outputed game
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "color_list.p")
    # pickle lets us dump this dataset into a file
    pickle.dump(unique_color_list, open(PICKLE_FILE, "wb"))


def get_existing_color_list(LEVELS_FOLDER):
    """This method will retrieve the list of unique colors from the levels directory of a game"""

    # declare the file we would like to load
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "color_list.p")
    # load the file using pickle
    unique_color_list = pickle.load(open(PICKLE_FILE, "rb"))

    return unique_color_list


def create_map(LEVELS_FOLDER, input_image, MAP_TITLE):
    """This method will save the map for the input level into the levels directory of the new game"""

    # contains a list of lists that represent the map
    map_list = utilities.get_color_map_list(input_image)
    # dump this list of lists to the levels folder of the game
    PICKLE_FILE = os.path.join(LEVELS_FOLDER, "{}.p".format(MAP_TITLE))
    pickle.dump(map_list, open(PICKLE_FILE, "wb"))


def add_map_to_project():
    """This method adds a new map to an existing game"""

    # new_lines contains data to be written to a file
    new_lines = []

    # the user will input some names for the existing project and name their
    # new map
    while True:
        GAME_TITLE = input("[addmap] Please enter the name of your project: ")

        # based on the GAME_TITLE we find the other needed directories
        GAME_FOLDER = os.path.join(OUTPUT_FOLDER, GAME_TITLE)
        GAME_FILE = os.path.join(GAME_FOLDER, GAME_TITLE + ".py")
        CLASS_FILE = os.path.join(GAME_FOLDER, "classes.py")
        LEVELS_FOLDER = os.path.join(GAME_FOLDER, "levels")

        # check to ensure these files exist
        if os.path.exists(GAME_FOLDER) and os.path.isfile(
                GAME_FILE) and os.path.isfile(CLASS_FILE) and os.path.exists(LEVELS_FOLDER):
            os.system('clear')
            break
        else:
            print("[addmap] necessary files have been renamed or removed.")
            print("[addmap] please ensure the correct name has been entered.\n")

    MAP_TITLE = input("[addmap] Please enter a title for your new map: ")

    # open the input image using the prompt below
    prompt = "\n[addmap] Please enter an image for the map: "
    input_image = utilities.get_image_if_valid(prompt, MAP_INPUT_FOLDER)

    # based on the gathered input we can create the map
    create_map(LEVELS_FOLDER, input_image, MAP_TITLE)

    # check if the new map contains a new color.
    old_colors = get_existing_color_list(LEVELS_FOLDER)
    new_colors = utilities.get_unique_color_list(input_image)

    # if there is a new color a flag is marked as true and two lists are
    # updated to contain these values
    updated_unique_color_list, new_tile_flag, new_colors = utilities.return_updated_list(
        old_colors, new_colors)

    # dump the list of unique colors to the levels folder
    set_unique_colors_list(LEVELS_FOLDER, updated_unique_color_list)

    # if we did find a new color, we need to create game code for it
    if new_tile_flag:
        color_dict = utilities.get_color_dict(new_colors)

        # attempt to update the classes.py file with new_lines based on the
        # color_dict
        try:
            print("[addmap] Loading the file: ", CLASS_FILE, "...\n")

            with open(CLASS_FILE) as reader:
                file = reader.readlines()

                for line in file:
                    # add all the pre-existing lines to new_lines
                    new_lines.append(line)

                    # if we find "load_data(self):" add the line of code that
                    # loads the new map
                    if "from settings import *" in line:
                        for color in color_dict:
                            new_lines.append("\n")
                            new_lines.append(
                                "class {}(pg.sprite.Sprite):\n".format(
                                    color_dict[color][0]))
                            new_lines.append(
                                "    def __init__(self, game, x, y):\n")
                            new_lines.append(
                                "        self.groups = game.background_sprites\n")
                            new_lines.append(
                                "        pg.sprite.Sprite.__init__(self, self.groups)\n")
                            new_lines.append("        self.game = game\n")
                            new_lines.append(
                                "        self.image = game.{}_img\n".format(
                                    color_dict[color][0]))
                            new_lines.append(
                                "        self.rect = self.image.get_rect()\n")
                            new_lines.append("        self.x = x\n")
                            new_lines.append("        self.y = y\n")
                            new_lines.append(
                                "        self.rect.x = x * TILE_SIZE\n")
                            new_lines.append(
                                "        self.rect.y = y * TILE_SIZE\n")

        # if we cannot update the file, the exception is caught and an error
        # message is returned
        except IOError:
            print(
                "\n[addmap] An IOError occured.  Perhaps the game file has been renamed or removed.\n")

        # write to the class file and then dump new_lines
        utilities.write_file(new_lines, CLASS_FILE)
        new_lines = []

    # regardless of a new color, the GAME_FILE needs updated.  This also uses
    # color_dict.
    try:
        print("[addmap] Loading the file: ", GAME_FILE, "...\n")

        with open(GAME_FILE) as reader:
            file = reader.readlines()

            for line in file:
                # add all the pre-existing lines to new_lines
                new_lines.append(line)

                # if we find "# load the map data", we can write the line of
                # code that loads the new map beneath this comment
                if "        # load the map data" in line:
                    #line = line.replace("\n", "")
                    new_lines.append(
                        "        self.{}_map = pickle.load(open(os.path.join(LEVELS_FOLDER, \"{}.p\"), \"rb\"))\n".format(
                            MAP_TITLE, MAP_TITLE))

                # if we find "# load the image data", we can write the lines of
                # code that load the image beneath this comment
                if "        # load the image data" in line and new_tile_flag:
                    for color in color_dict:
                        new_lines.append(
                            "        self.{}_img = pg.image.load(os.path.join(SPRITE_FOLDER, \"{}\"))\n".format(
                                color_dict[color][0], color_dict[color][1]))
                        new_lines.append(
                            "        self.{}_img = pg.transform.scale(self.{}_img, (TILE_SIZE, TILE_SIZE))\n".format(
                                color_dict[color][0], color_dict[color][0]))

                # if we find "# each color will load a specific tile", we can
                # write the line of code that places the images in pygame
                # beneath this comment
                if "                # each color will load a specific tile" in line and new_tile_flag:
                    for color in color_dict:
                        new_lines.append(
                            "                if color == {}:\n".format(color))
                        new_lines.append(
                            "                    {}(self, col, row)\n".format(
                                color_dict[color][0]))

    # if anything went wrong, the exception is caught and an error message is
    # printed
    except IOError:
        print(
            "\n[addmap] An IOError occured.  Perhaps the game file has been renamed or removed.\n")

    # write the new lines and then close the reader
    utilities.write_file(new_lines, GAME_FILE)


def create_pygame_classes(GAME_TITLE, NEW_GAME_FOLDER, color_dict):
    """This method will create pygame classes for each dictionary object"""

    print("[newgame] Creating PyGame classes...")

    # new_lines contains the data we will be writing to the output folder
    new_lines = ["import pygame as pg\n", "from settings import *\n"]

    # append data to new_lines.  This data is gathered from the color_dict.
    for color in color_dict:
        new_lines.append("\n")
        new_lines.append(
            "class {}(pg.sprite.Sprite):\n".format(
                color_dict[color][0]))
        new_lines.append("    def __init__(self, game, x, y):\n")
        new_lines.append("        self.groups = game.background_sprites\n")
        new_lines.append(
            "        pg.sprite.Sprite.__init__(self, self.groups)\n")
        new_lines.append("        self.game = game\n")
        new_lines.append(
            "        self.image = game.{}_img\n".format(
                color_dict[color][0]))
        new_lines.append("        self.rect = self.image.get_rect()\n")
        new_lines.append("        self.x = x\n")
        new_lines.append("        self.y = y\n")
        new_lines.append("        self.rect.x = x * TILE_SIZE\n")
        new_lines.append("        self.rect.y = y * TILE_SIZE\n")

    # declare a file in our new game called "classes.py"
    CLASS_FILE = os.path.join(NEW_GAME_FOLDER, "classes.py")
    # write the content of new_lines to the CLASS_FILE
    utilities.write_file(new_lines, CLASS_FILE)


def create_main_game_code(GAME_TITLE, NEW_GAME_FOLDER, color_dict, MAP_TITLE):
    """This method will create pygame code for the main game"""

    # data in new_lines will be written to a file with the GAME_TITLE inside a
    # directory of the NEW_GAME_FOLDER
    new_lines = ["import pygame as pg\n",
                 "import sys\n",
                 "import pickle\n",
                 "from settings import *\n",
                 "from classes import *\n",
                 "\n",
                 "class Game:\n",
                 "    def __init__(self):\n",
                 "        pg.init()\n",
                 "        self.screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))\n",
                 "        pg.display.set_caption(DISPLAY_TITLE)\n",
                 "        self.clock = pg.time.Clock()\n",
                 "        pg.key.set_repeat(1, 1)\n",
                 "        self.load_data()\n",
                 "        self.set_current_map(self.{}_map)\n".format(
                     MAP_TITLE),
                 "\n",
                 "    def load_data(self):\n",
                 "        # load the map data\n",
                 "        self.{}_map = pickle.load(open(os.path.join(LEVELS_FOLDER, \"{}.p\"), \"rb\"))\n".format(
                     MAP_TITLE, MAP_TITLE),
                 "\n",
                 "        # load the image data\n"]

    # iterates through the color_dict and pulls data.   Then uses .format() to
    # place this data in a line.
    for color in color_dict:
        new_lines.append(
            "        self.{}_img = pg.image.load(os.path.join(SPRITE_FOLDER, \"{}\"))\n".format(
                color_dict[color][0], color_dict[color][1]))
        new_lines.append(
            "        self.{}_img = pg.transform.scale(self.{}_img, (TILE_SIZE, TILE_SIZE))\n".format(
                color_dict[color][0], color_dict[color][0]))

    new_lines.append("\n")
    new_lines.append("    def new(self):\n")
    new_lines.append(
        "        # initialize all variables and do all the setup for a new game\n")
    new_lines.append("        self.background_sprites = pg.sprite.Group()\n")
    new_lines.append("\n")
    new_lines.append(
        "        # logic for drawing tiles from a list of lists\n")
    new_lines.append(
        "        for row, colors in enumerate(self.current_map):\n")
    new_lines.append("            for col, color in enumerate(colors):\n")
    new_lines.append(
        "                # each color will load a specific tile\n")

    # iterates through the color_dict and pulls data.   Then uses .format() to
    # place this data in a line.
    for color in color_dict:
        new_lines.append("                if color == {}:\n".format(color))
        new_lines.append(
            "                    {}(self, col, row)\n".format(
                color_dict[color][0]))

    new_lines.append("\n")
    new_lines.append("    def set_current_map(self, map_data):\n")
    new_lines.append(
        "        # TODO: use this method to change the current map\n")
    new_lines.append("        self.current_map = map_data\n")

    new_lines.append("\n")
    new_lines.append("    def run(self):\n")
    new_lines.append(
        "        # game loop - set self.playing = False to end the game\n")
    new_lines.append("        self.playing = True\n")
    new_lines.append("        while self.playing:\n")
    new_lines.append(
        "            self.dt = self.clock.tick(DISPLAY_FPS) / 1000\n")
    new_lines.append("            self.events()\n")
    new_lines.append("            self.update()\n")
    new_lines.append("            self.draw()\n")

    new_lines.append("\n")
    new_lines.append("    def quit(self):\n")
    new_lines.append("        pg.quit()\n")
    new_lines.append("        sys.exit()\n")

    new_lines.append("\n")
    new_lines.append("    def update(self):\n")
    new_lines.append("        # update portion of the game loop\n")
    new_lines.append("        self.background_sprites.update()\n")

    new_lines.append("\n")
    new_lines.append("    def draw(self):\n")
    new_lines.append("        self.screen.fill((0, 0, 0))\n")
    new_lines.append("        self.background_sprites.draw(self.screen)\n")
    new_lines.append("        pg.display.flip()\n")

    new_lines.append("\n")
    new_lines.append("    def events(self):\n")
    new_lines.append("        # catch all events here\n")
    new_lines.append("        pressed = pg.key.get_pressed()\n")
    new_lines.append("        for event in pg.event.get():\n")
    new_lines.append("            if event.type == pg.QUIT:\n")
    new_lines.append("                self.quit()\n")
    new_lines.append("            if event.type == pg.KEYDOWN:\n")
    new_lines.append("                if event.key == pg.K_ESCAPE:\n")
    new_lines.append("                    self.quit()\n")

    new_lines.append("\n")
    new_lines.append("g = Game()\n")
    new_lines.append("while True:\n")
    new_lines.append("    g.new()\n")
    new_lines.append("    g.run()\n")

    # now that all the pygame code is appended to new_lines, create the file
    # and write to it
    GAME_FILE = os.path.join(NEW_GAME_FOLDER, "{}.py".format(GAME_TITLE))
    utilities.write_file(new_lines, GAME_FILE)
