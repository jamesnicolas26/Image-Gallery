import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")

        self.create_widgets()
        self.images = []
        self.current_index = 0

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, bg="grey")
        self.canvas.pack(expand=True, fill="both")

        self.prev_button = tk.Button(self.root, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load Images", command=self.load_images)
        self.load_button.pack(side=tk.BOTTOM, pady=10)

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.images = []
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    self.images.append(os.path.join(folder_path, file_name))
            if self.images:
                self.current_index = 0
                self.show_image(self.images[self.current_index])

    def show_image(self, image_path):
        image = Image.open(image_path)
        self.image_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def show_previous_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.show_image(self.images[self.current_index])

    def show_next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_image(self.images[self.current_index])

# Create the main window
root = tk.Tk()
app = ImageGallery(root)
root.mainloop()
