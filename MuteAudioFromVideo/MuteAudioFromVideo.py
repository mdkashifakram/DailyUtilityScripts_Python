from moviepy.editor import VideoFileClip

def mute_video(input_file, output_file):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Mute the audio
    muted_video = video.volumex(0)
    
    # Write the result to the output file
    muted_video.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Example usage
if __name__ == "__main__":
    input_video = "input_video.mp4"  # Replace with your input video file
    output_video = "muted_video.mp4"  # Specify the output file name
    mute_video(input_video, output_video)
