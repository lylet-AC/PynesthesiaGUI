from tkinter import *
from tkinter import filedialog
from settings import *


def get_file(start_path = ROOT_FOLDER):
    path = filedialog.askopenfilename(initialdir = start_path ,title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    return path

def get_folder(start_path = ROOT_FOLDER):
    path = filedialog.askdirectory(initialdir = start_path)
    return path

def open_proj():
    pass

def create_new_game():
    pass

def add_map_to_project():
    """adds a map to a specified project"""

    """set up first set of input"""

    # set up text
    text_one = Label(root, text = "Please provide the project path: ", height=2, width=30)
    text_one.grid(columnspan = 2, row = 0)

    # set up a textbox for appending to browsed input
    global proj_input_text
    proj_input_text = Entry(root, width = 45)
    proj_input_text.grid(row = 1, column = 0, padx = 5, pady = 5)

    # set up a button for getting the path
    proj_input_button = Button(text = "Browse", command = proj_button_action, width = 10)
    proj_input_button.grid(row = 1, column = 1, padx = 5, pady = 5)

    """set up second set of input"""

    # set up text again
    text_two = Label(root, text = "Please provide the image path: ", height=2, width=30)
    text_two.grid(columnspan = 2, row = 4)

    # set up a textbox for appending to browsed input
    global image_input_text
    image_input_text = Entry(root, width = 45)
    image_input_text.grid(row = 5, column = 0, padx = 5, pady = 5)

    # set up a button for getting the path
    image_input_button = Button(text = "Browse", command = image_button_action, width = 10)
    image_input_button.grid(row = 5, column = 1, padx = 5, pady = 5)

def proj_button_action():
    """the logic for the proj_input_button"""
    filepath = get_folder(OUTPUT_FOLDER)
    temp = proj_input_text.get()
    proj_input_text.delete(0, len(temp))
    proj_input_text.insert(0, filepath)

def image_button_action():
    """the logic for the proj_input_button"""
    filepath = get_file(MAP_INPUT_FOLDER)
    temp = image_input_text.get()
    image_input_text.delete(0, len(temp))
    image_input_text.insert(0, filepath)

def configure_gui():
    pass

root = Tk()

# set up the window
root.geometry('500x300')
root.title('Pynesthesia')

# construct menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

# add some commands to file
filemenu.add_command(label="New...", command=create_new_game)
filemenu.add_command(label="Open...", command=open_proj)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# add some commands to edit
editmenu.add_command(label="Add Map...", command=add_map_to_project)
editmenu.add_separator()
editmenu.add_command(label="Preferences", command=configure_gui)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
