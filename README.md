# Pynesthesia

Pynesthesia is an open source code generation tool that allows a user to generate the game code for a simple tile-based game map by using an input image.  This program then converts that input image to Pygame code with each pixel corresponding to a unique tile, and each color corresponding to a specific class on which the tiles are loaded into the game.  The two most important pieces of information the user will input for each detected color will be the class name, as well as an image for the tile when displayed in the game.  Pynesthesia is written in Python and outputs Python Pygame code.  The code that is output is set up to be easily modified by the user to create a game.

## Installation

Pynesthesia is a program written in Python 3.  Pip3 is the default package installer that comes with Python and therefore, it is required to install other dependencies for this program.    Pynesthesia supports three primary types of operating systems: **Ubuntu**, **Windows**, and **Mac OSX**; and other operating systems that can run software that support these systems.  Depending on your operating system, dependencies such as Python3, Pip3, and Tkinter will require a different set of instructions for setup.  

### Linux Distributions

In most Linux distributions, Python comes pre-installed with the operating system.  Verifying that Python is installed is as simple as typing the following command into the terminal: `python3 --version`.  If Python3 is not installed, the terminal will usually give a command for installing Python3.  Alternatively, you can chose to use those instructions, or type in the following commands:
```
sudo apt-get update
sudo apt-get install Python3
```

To handle Python specific dependencies, Python uses Pip3.  Use `pip3 --version` to verify if Pip3 was installed as apart of your Python installation.  If it was not installed, use the following commands to install it:
```
sudo apt-get install python-pip
```
Next, Pynesthesia uses the Tkinter package to handle the creation of the user interface.  To install this package in most Linux distributions, type:

```
sudo apt-get install python-tk
```
Then verify the installation by typing in `python3` into the terminal.  Once the Python interpreter opens, type `import tkinter`.  If no error occurs, then the tkinter package was successfully installed and you may now begin using Pynesthesia.

### Windows

If you are a windows user and need to install Python3 / tkinter / Pip3, [download](https://www.python.org/downloads/windows/) the python3 installation file.  This file is capable of installing Python3, tkinter, and Pip3 given the correct boxes are checked. Meaning that one must ensure upon installing Python that **the td/tk and IDLE checkboxes are marked for installing tkinter and Pip3 with Python.** Pynesthesia specifically uses `Python 3.6.7`, although other iterations of Python3 should work properly as well.

### Mac OSX

Much like Linux, Python3 is included in the Mac OSX installation.  However, to keep Python3 updated, [download](https://www.python.org/downloads/mac-osx/) the relevant version of the Python3 binary.  These work similarly to its Windows counterpart, and one must ensure that **the tcl/tk and IDLE checkboxes are marked for installing tkinter and Pip3 with Python.**  After the installer has finished installing Python3 to your machine, you are ready to use Pynesthesia.

## Using Pynesthesia

Pynesthesia uses a requirements.txt file to automatically install all of the necessary dependencies with pip3.  To install the requirements, run the following commands in the root directory of Pynesthesia after ensuring Python3 has been properly installed:

 ```
 pip3 install --upgrade pip
 pip3 install --user -r requirements.txt
 ```

Next run Pynesthesia itself with:

 ```
 python3 Pynesthesia.py
 ```

Using Pynesthesia is as easy as following the on screen prompts that show up on the screen.  These prompts are set up as a Read-Eval-Print_Loop or REPL.  In REPL functionality, the main design feature is command driven actions.  This means that Pynesthesia has a set of known commands that correspond to different features of the program.  When first starting Pynesthesia, it mentions that a new user may want to type `help`.  If the user types `help` then a list of commands are printed.

 These commands are as follows:
 - `help` - prints a list of commands
 - `newgame` - follow the prompts to create a new Pygame game
 - `confset` - configure the default game settings
 - `addmap` - follow the prompts to add a map to an existing Pynesthesia game
 - `howto` - a detailed description of how to use Pynesthesia


It is first recommended to use the `confset` command to configure the settings of your new game. Alternatively, attributes can be edited manually by opening the `settings.py` file in a text editor and changing appropriate values by hand.  It is, however, important to note that the directories listings in the settings file should not be edited with an explanation given in the next section.  Settings below the `"""Game settings here"""` docstring are the ones that are configurable without issue.

There is also a quirk with Pynesthesia and any created game sharing the same settings file.  This means that Pynesthesia uses the directories the same way the generated game does.

### Editing and Changing Filenames

Pynesthesia expects a certain directories and inputs from the user in order to achieve it's goal.  First, Pynesthesia expects the input image (which will become the map) to be located in the `input` directory; and all images that will be used for the in game tiles to be located in the `sprites` directory.  When attempting to access an image that doesn't exist, Pynesthesia will prompt the user that the image does not exist and print out the directory it expects the image to be in.  This mostly effects the `newgame` and `addmap` commands.

Secondly, Pynesthesia generates the Pygame code in a directory specified by the user.  Methods in Pynesthesia gather this data as user input. The user is free to remove their created game from the output directory, however, methods such as `addmap` and `confset` gather this data as user input.  This means that the created game directory must be placed back in the output directory prior to using Pynesthesia to edit the project.  This also means that certain things cannot be renamed or else Pynesthesia will not be able to find files appropriately.  Therefore, the user should not rename or remove generated folders, python files, or remove or rename comments in the generated code.

## Testing Pynesthesia

Pynesthesia uses the Python test suite Pytest.  A test suite allows the code to be automatically checked for errors and bugs when ran in combination with Travis CI.  Using the GitHub flow model, any new code added to Pynesthesia is done through branches (or forks).  For a feature branch to be pushed to master, it must first have passing test cases for each new function in the branch.  Pynesthesia is configured with Travis CI, meaning that test cases are checked upon pushing to a branch.  **Pull requests that do not meet these requirements will not be merged with master.**

Pytest needs to be installed separately from the Python installation by entering the command: `pip3 install pytest`.  Once Pytest has successfully installed, it is good practice to verify the installation by typing in the command: `pytest --version`.  To then run the test cases for Pynesthesia, first navigate to the Pynesthesia directory.  In a terminal or cmd window, type:
```
python3 -m pytest tests
```

## Coming in Future Updates

Below is a list of features that may be added in future updates:
 - Tkinter user interface
 - Include code coverage into the test suite
 - Built in player class template
 - Built in camera class template
 - Parallax scrolling capabilities
 - Built in tile loading and tile unloading
 - Animations for tiles
