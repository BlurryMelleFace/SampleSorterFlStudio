import os
import shutil
import tkinter as tk  

# Specify the path to the samples directory and the destination directory
samples_dir = r"C:\Users\morit\Documents\Local Samples\Big Samplepacks"
dest_dir = r"C:\Users\morit\Documents\Local Samples\Sorted"

shutil.rmtree(dest_dir, ignore_errors=True, onerror=os.remove)

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
    "FX": ["fx","downfilter","upfilter","reverse","rev","sweep","noise","downsweep","upsweep","impact","uplifter"],
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

# Find all audio files in the samples directory (including subdirectories)
audio_files = find_audio_files(samples_dir)

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

