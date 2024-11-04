import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Video Player")
        self.video_path = None
        self.cap = None

        # Create canvas to display video frames
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        # Buttons for controls
        self.btn_open = tk.Button(root, text="Open Video", command=self.open_video)
        self.btn_open.pack()

        self.btn_play = tk.Button(root, text="Play", command=self.play_video, state=tk.DISABLED)
        self.btn_play.pack()

        self.btn_pause = tk.Button(root, text="Pause", command=self.pause_video, state=tk.DISABLED)
        self.btn_pause.pack()

        self.is_paused = False

    def open_video(self):
        # File dialog to open a video file
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.btn_play.config(state=tk.NORMAL)

    def play_video(self):
        if not self.is_paused:
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_play.config(state=tk.DISABLED)
            self.show_frame()

    def show_frame(self):
        if self.cap and not self.is_paused:
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame to an ImageTk object
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                # Update canvas with new frame
                self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                self.root.update()
                
                # Keep reference to prevent garbage collection
                self.canvas.imgtk = imgtk

                # Call show_frame recursively
                self.canvas.after(10, self.show_frame)
            else:
                self.cap.release()

    def pause_video(self):
        self.is_paused = not self.is_paused
        self.btn_pause.config(text="Resume" if self.is_paused else "Pause")
        if not self.is_paused:
            self.show_frame()

# Create tkinter window
root = tk.Tk()
player = VideoPlayer(root)
root.mainloop()
