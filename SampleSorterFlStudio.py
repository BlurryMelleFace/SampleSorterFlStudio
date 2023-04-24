import os
import shutil
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog  
import tkinter.messagebox as messagebox


# Specify the path to the samples directory and the destination directory

samples_dir = r""
dest_dir = r""

shutil.rmtree(dest_dir, ignore_errors=True, onerror=os.remove)

# create the window
root = tk.Tk()
root.title("Sample Sorter")
root.iconbitmap(r'C:\Users\morit\OneDrive\Hobbies\CodingProjects\SampleSorterFlStudio\FL.ico')

# Define a function to search for audio files in a directory (including subdirectories)

def find_audio_files(directory):
    audio_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac", ".aif")):
                audio_files.append(os.path.join(dirpath, filename))
    return audio_files

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

def findAudioFiles(*args):
    global audio_files
    audio_files = find_audio_files(samples_dir)
    filesFoundLabel.configure(text="Amount: {}".format(int(len(audio_files))))
    
def standardInsert():
    entry.insert(0,r"C:\Users\morit\Documents\Coding Test\Sample Sorter\Sample Test")
    entry2.insert(0,r"C:\Users\morit\Documents\Coding Test\Sample Sorter\Sorted")

frame = tk.Frame(root)
frame.pack()

directoryFrame = tk.LabelFrame(frame, text="Directory Selection")
directoryFrame.grid(row= 0, column=0, padx= 20, pady=10, sticky="NSEW")

sampleLabel = tk.Label(directoryFrame, text="Sample Directory")
sampleLabel.grid(row=0, column=0)
destinationLabel = tk.Label(directoryFrame, text="Destination Directory")
destinationLabel.grid(row=0, column=1)

entryString = tk.StringVar()
entryString.trace("w", entryOnChange)
entry = tk.Entry(directoryFrame, textvariable = entryString, width=80)
entry.grid(row=1, column=0, padx= 5, pady=5)

entry2String =tk.StringVar()
entry2String.trace("w", entry2OnChange)
entry2 = tk.Entry(directoryFrame, textvariable = entry2String, width=80)
entry2.grid(row=1, column=1, padx= 5, pady=5)

button = tk.Button(directoryFrame,text="Select Sample Directory", command= getSampleDirectory)
button.grid(row=2, column=0, padx= 5, pady=5)

button2 = tk.Button(directoryFrame,text="Select Destination Directory", command= getDestDirectory)
button2.grid(row=2, column=1, padx= 5, pady=5)

# Standard 

standardFrame = tk.LabelFrame(frame, text="Standard")
standardFrame.grid(row= 6, column=0, padx= 20, pady=10, sticky="NSEW")

buttonStand1= tk.Button(standardFrame,text="Standard", command= standardInsert)
buttonStand1.grid(row=0, column=0, padx= 5, pady=5)

# Progress Frame 

progressFrame = tk.LabelFrame(frame, text="Progress")
progressFrame.grid(row= 4, column=0, padx= 20, pady=10, sticky="NSEW")
progressFrame.columnconfigure(0, weight=1) # weight 1 to dynamically ajust

# Progress1

progressbar1Progress= ttk.Progressbar(progressFrame, orient="horizontal", mode="determinate")
progressbar1Progress.grid(row=0, column=0, padx= 5, pady=5, sticky="EW")

labelProgress1 =tk.Label(progressFrame, text= "Copied: ")
labelProgress1.grid(row=0,column=1, padx= 5, pady=5)

#Progress2

progressbar2Progress= ttk.Progressbar(progressFrame, orient="horizontal", mode="determinate")
progressbar2Progress.grid(row=1, column=0, padx= 5, pady=5, sticky="EW")

labelProgress2 =tk.Label(progressFrame, text= "Identified: ")
labelProgress2.grid(row=1,column=1, padx= 5, pady=5)

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
    "FX": ["fx","downfilter","upfilter","reverse","rev","sweep","noise","downsweep","upsweep","impact","Uplifter","buildup"],
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
    "Ambiance": ["ambiance"],
    "Vinyl": ["Vinyl"]
}

# Loop through all categories

def sortingAlgorithm():
    
    if not dest_dir and not samples_dir:
        messagebox.showerror("Error", "Please select both directories.")
        return    
    elif not dest_dir:
        messagebox.showerror("Error", "Please select the destination directory.")
        return
    elif not samples_dir:
        messagebox.showerror("Error", "Please select the sample directory.")
        return
    
    # Find all audio files in the samples directory (including subdirectories)

    audio_files = find_audio_files(samples_dir)
    findAudioFiles()

    # Progressbar

    progressbar1Progress['value'] = 0
    progressbar2Progress['value'] = 0

    progressbar1Amount = 0
    progressbar2Amount = 0    

    labelProgress2.configure(text="Identified: {}%  | {}".format(int(progressbar2Progress['value']), int(progressbar2Amount)))
    labelProgress1.configure(text="Copied: {}%  | {}".format(int(progressbar1Progress['value']),int(progressbar1Amount)))

    if (len(audio_files) == 0):
        messagebox.showerror("Error", "Cant Sort with 0 Samples")
        
    progressIteration = 100/len(audio_files)

    if not audio_files:
        messagebox.showerror("Error", "No Samples Found")
        return       

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
                    
                    #Progressbar 2
                    progressbar2Progress['value'] += progressIteration
                    progressbar2Amount += 1
                    root.update_idletasks()
                    labelProgress2.configure(text="Identified: {}%  | {}".format(int(progressbar2Progress['value']), int(progressbar2Amount)))

                    if not os.path.exists(dest_path):      
                        # Update the Progressbar
                        progressbar1Progress['value'] += progressIteration
                        progressbar1Amount += 1

                        root.update_idletasks()                                           
                        shutil.copy(file_path, dest_path)   
                        print(filename)   
                    elif os.path.exists(dest_path):
                        deviationlistbox.insert(tk.END,filename)
                        print("******" +filename)
                    labelProgress1.configure(text="Copied: {}%  | {}".format(int(progressbar1Progress['value']),int(progressbar1Amount)))
                        
                

    # iterate through each item in the directory
    for item in os.listdir(dest_dir):
        # construct the full path for the item
        item_path = os.path.join(dest_dir, item)
        # check if the item is a directory and if it's empty
        if os.path.isdir(item_path) and not os.listdir(item_path):
            # if it's empty, delete it
            os.rmdir(item_path)


    messagebox.showinfo(None, "Finished!")


filesFoundFrame = tk.LabelFrame(frame, text="Files Found")
filesFoundFrame.grid(row= 1, column=0, padx=20, pady=10, sticky="NSEW")

filesFoundButton = tk.Button(filesFoundFrame, text="Search", command = findAudioFiles)
filesFoundButton.grid(row=0, column=0, padx= 5, pady=5)

filesFoundLabel = tk.Label(filesFoundFrame, text="Amount: ")
filesFoundLabel.grid(row=0, column=1, padx= 5, pady=5)

# Category Frame

categoryFrame = tk.LabelFrame(frame, text="Categories")
categoryFrame.grid(row= 2, column=0, padx=20, pady=10, sticky="NSEW")

buttonCategory = tk.Button(categoryFrame,text="Start")
buttonCategory.grid(row=0, column=1, padx= 5, pady=5)

# Start Frame

startFrame = tk.LabelFrame(frame, text="Start")
startFrame.grid(row= 3, column=0, padx= 20, pady=10, sticky="NSEW")

button3 = tk.Button(startFrame,text="Start", command= sortingAlgorithm)
button3.grid(row=0, column=1, padx= 5, pady=5)

# Deviation Frame

deviationFrame = tk.LabelFrame(frame, text="Deviations")
deviationFrame.grid(row= 5, column=0, padx= 20, pady=10, sticky="NSEW")

deviationscrollbar = tk.Scrollbar(deviationFrame)
deviationscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

deviationlistbox = tk.Listbox(deviationFrame, yscrollcommand=deviationscrollbar.set, width= 100)
deviationlistbox.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

deviationscrollbar.config(command=deviationlistbox.yview)

# Run the main loop
root.mainloop()  

