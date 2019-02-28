from PIL import Image
import os
# local imports
from settings import *


def get_path_if_valid(prompt, type="file", path=""):
    """This method ensures that a file exists and returns the filepath if it does"""

    while True:

        file = input(prompt)
        full_path = os.path.join(path, file)

        # if we are looking for a directory
        if type == "directory":
            if os.path.exists(full_path):
                return full_path
            else:
                print("[utilities] That directory does not exist:\n")
                print(full_path)

        # if we are looking for a file
        elif type == "file":
            if os.path.isfile(full_path):
                return full_path
            else:
                print("[utilities] That file does not exist at:\n")
                print(full_path)


def get_image_if_valid(prompt, path=""):
    """This method will ask the user a prompt and return an loaded PIL image"""

    # iterate through the while loop until correct input is gathered
    while True:

        # try to get the input image
        try:
            INPUT_IMAGE_PATH = get_path_if_valid(prompt, path=path)
            image = Image.open(INPUT_IMAGE_PATH)

        # if bad input is entered, an exception is thrown and caught here
        except BaseException as e:
            print("[newgame] This file is not a supported format.")
            print(e)

        # if we do not encounter an exception break the loop
        else:
            return image


def get_color_dict(unique_color_list, ignore_valid_files=False):
    """This method takes a list of colors and asks the user for input"""

    color_dict = {}

    for color in unique_color_list:
        os.system('clear')
        object_name = input(
            "[utilities] What would you like color {} to represent? ".format(color))

        EXIT = False

        # iterate through the while loop until correct input is gathered
        while EXIT is False:

            # try to get the sprite image
            try:
                object_image_path = input(
                    "\n[utilities] Please provide the image for this object: ")

                if ignore_valid_files is False:
                    test_open = Image.open(
                        os.path.join(
                            SPRITE_FOLDER,
                            object_image_path))

                color_dict[color] = [object_name, object_image_path]

                EXIT = True

            # if bad input is entered, an exception is thrown and caught here
            except BaseException:
                print(
                    "[utilities] This image is not a supported format or does not exist.")
                print(
                    "[utilities] Please insert the image into the 'sprites' directory and try again.\n")

    return color_dict


def get_unique_color_list(input_image):
    """This method obtains a list of unique colors in the input list"""
    pix = input_image.load()

    unique_list = []

    width, height = input_image.size

    for w in range(width):
        for h in range(height):
            if pix[w, h] not in unique_list:
                unique_list.append(pix[w, h])

    return unique_list


def get_color_map_list(input_image):
    """This method gathers a representation of the input image as list of lists containing the color data for each line of the input image"""
    pix = input_image.load()

    map_list = []

    width, height = input_image.size

    for w in range(width):
        map_list.append([])
        for h in range(height):
            map_list[w].append(pix[h, w])

    return map_list


def return_updated_list(old_color_list, new_color_list):
    """This method compares two lists and finds values that are not apart of the first list, but are in the second"""

    new_tile_flag = False
    new_colors = []

    for color in new_color_list:
        if color not in old_color_list:
            old_color_list.append(color)
            new_colors.append(color)
            new_tile_flag = True

    return old_color_list, new_tile_flag, new_colors


def write_file(new_lines, file_name):
    """This method writes information in the form of a list of lines to the file specified by file_name"""

    try:
        print("\n[utilities] Writing the file: ", file_name, "...")
        file = open(file_name, "w")

        for line in new_lines:
            file.write(line)

        file.close()

        print("[utilities] Done!\n")

    except BaseException:
        print("\n[utilities] Writing the file encountered an error.\n")
