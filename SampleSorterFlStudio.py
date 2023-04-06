import os
import shutil
import re

# Specify the path to the samples directory and the destination directory
samples_dir = r"C:\Users\morit\Documents\Local Samples\Big Samplepacks\Trap Samples\BEsomorph"
dest_dir = r"C:\Users\morit\Desktop\Sorting Test"

# Create a dictionary of categories and their corresponding keywords
categories = {
    "Drums": ["kick"],
    "Kicks": ["kick"],
    "Snare": ["snare"],
    "Clap": ["clap"],
    "Perc": ["perc","percussive"],
    "FX": ["fx","downfilter","upfilter"],
    "Hats":["hat","hihat"],
    "Vocal": ["vox","vocal"],
    "808":["808"]
}

# Define a function to search for audio files in a directory (including subdirectories)
def find_audio_files(directory):
    audio_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac")):
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
        
        words = filename.split(" ")
        
        # Loop through all the words in the filename
        for word in words:
            # Check if the word is a keyword for the current category
            assert(isinstance(word, str))
            if word.split(".")[0].lower() in keywords:
                # Copy the file to the corresponding category folder
                dest_path = os.path.join(category_path, filename)
                shutil.copy(file_path, dest_path)         




# Using Regexes
# print(f"Copied file: {word.lower()}, {category_path}, {filename}, {file_path}, {dest_path}") 
# c = "hallo/welt.wave"
# m = re.search("welt", c)
# if isinstance(m ,re.Match):
#     print("Match!")
