# import package
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk


class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.set_theme("default")
        self.root.title("CDY Media Player")
        self.root.geometry("500x200")

        self.media_file = ""
        self.playing = False

        self.initialize_gui()

    def initialize_gui(self):
        frame1 = ttk.Frame(self.root)
        frame1.pack(side="left", fill="y", padx=5, pady=5)

        self.play_button = ttk.Button(frame1, text="Play", command=self.play_pause)
        self.play_button.pack()

        self.pause_button = ttk.Button(frame1, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = ttk.Button(frame1, text="Stop", command=self.stop)
        self.stop_button.pack()

        frame2 = ttk.Frame(self.root)
        frame2.pack(side="left", fill="y", padx=5, pady=5)

        self.next_button = ttk.Button(frame2, text="Next", command=self.next_track)
        self.next_button.pack()

        self.prev_button = ttk.Button(frame2, text="Previous", command=self.prev_track)
        self.prev_button.pack()

        self.status_label = ttk.Label(self.root, text="No media file selected")
        self.status_label.pack(fill="x", padx=5, pady=5)

        ttk.Separator(self.root, orient="vertical").pack(side="left", fill="y")

        self.open_button = ttk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack(fill="x", padx=5, pady=5)

        ttk.Separator(self.root, orient="vertical").pack(side="left", fill="y")

        self.volume_scale = ttk.Scale(self.root, from_=0, to=1, orient="vertical", command=self.set_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(fill="y", padx=5, pady=5)

    def open_file(self):
        self.media_file = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp3 *.mp4 *.avi *.mkv *.wav")])
        if self.media_file:
            self.status_label.config(text="Playing: " + self.media_file)

    def play_pause(self):
        if not self.media_file:
            return
        if not self.playing:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(self.media_file)
            pygame.mixer.music.set_volume(self.volume_scale.get())
            pygame.mixer.music.play()
            self.playing = True
            self.status_label.config(text="Playing: " + self.media_file)
        else:
            pygame.mixer.music.unpause()
            self.playing = True
            self.status_label.config(text="Playing: " + self.media_file)

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
            self.status_label.config(text="Paused: " + self.media_file)

    def stop(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.status_label.config(text="No media file selected")

    def set_volume(self, val):
        if self.playing:
            pygame.mixer.music.set_volume(float(val))

    def next_track(self):
        # Implement logic to play the next track in the playlist
        pass

    def prev_track(self):
        # Implement logic to play the previous track in the playlist
        pass

if __name__ == "__main__":
    root = ThemedTk(theme="clearlooks")
    player = MediaPlayer(root)
    root.mainloop()
