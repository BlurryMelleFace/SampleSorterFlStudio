import os
import shutil
import tkinter as tk
from tkinter import filedialog  
import tkinter.messagebox as messagebox

# Specify the path to the samples directory and the destination directory

samples_dir = r""
dest_dir = r""

shutil.rmtree(dest_dir, ignore_errors=True, onerror=os.remove)

# create the window
root = tk.Tk()


# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# calculate the x and y coordinates of the window
x = (screen_width // 2) - (WINDOW_WIDTH // 2)
y = (screen_height // 2) - (WINDOW_HEIGHT // 2)

# set the window size and position
root.geometry('{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y))

#functions for the buttons
def getSampleDirectory():
    entry.delete(0,tk.END)
    global samples_dir
    entry.insert(0,filedialog.askdirectory())

def getDestDirectory():
    entry2.delete(0,tk.END)
    global dest_dir
    dest_dir = filedialog.askdirectory() + "/Sorted"
    entry2.insert(0,dest_dir)

def entryOnChange(*args):
    global samples_dir
    samples_dir = entryString.get()
    print(samples_dir)
    

def entry2OnChange(*args):
    global dest_dir
    dest_dir = entry2String.get()
    print(dest_dir)
    
# Create a label widget with a default font size
  
frame = tk.Frame(root)
frame.pack()

entryString = tk.StringVar()
entryString.trace("w", entryOnChange)
entry = tk.Entry(frame, width = 200, textvariable= entryString)
entry.pack()

entry2String =tk.StringVar()
entry2String.trace("w", entry2OnChange)
entry2 = tk.Entry(frame, width = 200, textvariable= entry2String)
entry2.pack()

button = tk.Button(text="Select Sample Directory", command= getSampleDirectory)
button.pack()

button2 = tk.Button(text="Select Destination Directory", command= getDestDirectory)
button2.pack()

# Create a dictionary of categories and their corresponding keywords
categories = {
    "Drums": ["Drum","drums"],
    "Kicks": ["kick"],
    "Snare": ["snare"],
    "Clap": ["clap","claps"],
    "Toms": ["tom","toms"],
    "Crash": ["crash"],
    "Snaps": ["snap","Snaps"],
    "Fills": ["fill", "fills"],
    "Hits": ["hit","hits"],
    "Shaker": ["shake","shaker"],
    "Rides": ["rides","ride"],
    "MelodyLoops": ["melody","Guitar","piano","string",],
    "Rim": ["rim"],
    "Cymbal": ["cymbal"],
    "Perc": ["perc","percussive","percussion"],
    "FX": ["fx","downfilter","upfilter","reverse","rev","sweep","noise","downsweep","upsweep","impact","Uplifter"],
    "Hats":["hat","hihat"],
    "Top": ["top"],
    "Vocal": ["vox","vocal","vocoder"],
    "Chants": ["chant", "chants"],
    "Glass": ["glass"],
    "808":["808"],
    "Misc": ["misc"],
    "Horns": ["horn","horns"],
    "Stabs": ["stab","stabs"],
    "Foley": ["foley"],
    "Ambiance": ["ambiance"]
}

# Define a function to search for audio files in a directory (including subdirectories)
def find_audio_files(directory):
    audio_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac", ".aif")):
                audio_files.append(os.path.join(dirpath, filename))
    return audio_files

# Loop through all categories
def sortingAlgorithm():
    if not dest_dir and not samples_dir:
        messagebox.showerror("Error", "Please select both destination directories.")
        return    
    elif not dest_dir:
        messagebox.showerror("Error", "Please select the destination directory.")
        return
    elif not samples_dir:
        messagebox.showerror("Error", "Please select the sample directory.")
        return
    
    # Find all audio files in the samples directory (including subdirectories)
    audio_files = find_audio_files(samples_dir)

    print(audio_files)

    # Loop through all categories
    for category, keywords in categories.items():

        # Create the corresponding category folder if it doesn't exist
        category_path = os.path.join(dest_dir, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Loop through all audio files
        for file_path in audio_files:
            # Get the filename without the path
            filename = os.path.basename(file_path)

            # Split the filename into words
            words = filename.split()
            
            # Loop through all the words in the filename
            for word in words:
                # Check if the word is a keyword for the current category
                assert(isinstance(word, str))
                if word.split(".")[0].lower() in keywords:
                    # Copy the file to the corresponding category folder
                    dest_path = os.path.join(category_path, filename)
                    if not os.path.exists(dest_path):
                        shutil.copy(file_path, dest_path)   
                        print(filename)

    # iterate through each item in the directory
    for item in os.listdir(dest_dir):
        # construct the full path for the item
        item_path = os.path.join(dest_dir, item)
        # check if the item is a directory and if it's empty
        if os.path.isdir(item_path) and not os.listdir(item_path):
            # if it's empty, delete it
            os.rmdir(item_path)


    messagebox.showinfo(None, "Finished!")

button3 = tk.Button(text="Start", command= sortingAlgorithm)
button3.pack()

# Run the main loop
root.mainloop()  

