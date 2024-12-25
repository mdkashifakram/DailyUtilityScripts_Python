from moviepy.editor import VideoFileClip

def speed_up_video(input_path, output_path, speed_factor):
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Speed up the video by the given factor
    sped_up_clip = clip.fx(lambda c: c.speedx(factor=speed_factor))
    
    # Write the output video file
    sped_up_clip.write_videofile(output_path, codec="libx264")

# Example usage
input_video = "input_video.mp4"   # Path to your input video
output_video = "output_video.mp4" # Path to save the sped-up video
speed_factor = 2.0                # Factor by which to speed up the video (e.g., 2.0 doubles the speed)

speed_up_video(input_video, output_video, speed_factor)
