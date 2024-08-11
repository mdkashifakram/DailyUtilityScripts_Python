import os
from moviepy.editor import *

def convert_to_mp3(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of files in input folder
    files = os.listdir(input_folder)

    for file in files:
        if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mov"):
            video_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")

            # Convert video to audio
            video = VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(output_path)

            # Close video file
            video.close()

if __name__ == "__main__":
    input_folder = input("Enter the path of the folder containing videos: ")
    output_folder = input("Enter the path where you want to save the converted mp3 files: ")

    convert_to_mp3(input_folder, output_folder)
