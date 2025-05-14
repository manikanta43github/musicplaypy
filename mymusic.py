import pygame
import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label
import os

pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")

        self.playlist = Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist.pack(pady=10, fill=tk.BOTH, expand=True)

        self.load_button = Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack()

        self.play_button = Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.stop_button = Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

    def load_music(self):
        file_path = filedialog.askdirectory()
        if file_path:
            for song in os.listdir(file_path):
                if song.endswith(".mp3"):
                    self.playlist.insert(tk.END, os.path.join(file_path, song))

    def play_music(self):
        selected_song = self.playlist.get(tk.ACTIVE)
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
