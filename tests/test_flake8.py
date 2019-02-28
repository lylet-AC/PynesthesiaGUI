# code was written with help from the gatorgrouper repository

import glob
import os
from flake8.api import legacy as flake8


def test_flake8():
    """ test python files align to flake8 standards """

    # list of all file names to be checked for PEP8
    name_of_files = []

    # fill list with all python files found in all subdirectories
    for root, _, files in os.walk("Pynesthesia", topdown=False):
        files = glob.glob(root + "/../*.py")
        name_of_files.extend(files)

    style_guide = flake8.get_style_guide(ignore=[
        "E265", "E501", "E101", "W191", 'E402', 'E501', 'F405'])
    report = style_guide.check_files(name_of_files)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
