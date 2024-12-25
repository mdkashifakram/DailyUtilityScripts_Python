from moviepy.editor import VideoFileClip, concatenate_videoclips

def mute_video(input_video_path, output_video_path, mute_start_time, mute_end_time):
    # Load the video file
    video = VideoFileClip(input_video_path)

    # Split the video into 3 parts: before mute, mute section, and after mute
    part1 = video.subclip(0, mute_start_time)  # Part before mute
    part2 = video.subclip(mute_start_time, mute_end_time).volumex(0)  # Muted part
    part3 = video.subclip(mute_end_time)  # Part after mute

    # Concatenate the parts
    final_video = concatenate_videoclips([part1, part2, part3])

    # Write the final video to an output file
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# Example usage
input_video = "input.mp4"
output_video = "output_video.mp4"
mute_start = 57  # Mute start time in seconds
mute_end = 58   # Resume audio at 1 minute 40 seconds

mute_video(input_video, output_video, mute_start, mute_end)
