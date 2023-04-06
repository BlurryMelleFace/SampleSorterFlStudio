import os
import shutil

# Specify the path to the samples directory and the destination directory
samples_dir = r"C:\Users\morit\Documents\Local Samples\Big Samplepacks\Trap Samples\BEsomorph"
dest_dir = r"C:\Users\morit\Desktop\Sorting Test"

# Create a dictionary of keywords and their corresponding folders
folders = {
    "kick": "Kicks",
    "snare": "Snares",
    "clap": "Claps",
    "hihat": "Hihats",
    "perc": "Percussion",
    "fx": "FX",
    "vocal": "Vocals",
    "synth": "Synths"
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

# Loop through all audio files
for file_path in audio_files:
    # Get the filename without the path
    filename = os.path.basename(file_path)

    # Split the filename into words
    words = filename.split()

    # Loop through all the words in the filename
    for word in words:
        # Check if the word is a keyword
        if word.lower() in folders:
            # If it is, create the corresponding folder if it doesn't exist
            folder_path = os.path.join(dest_dir, folders[word.lower()])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Copy the file to the corresponding folder
            dest_path = os.path.join(folder_path, filename)
            shutil.copy(file_path, dest_path)
