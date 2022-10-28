from tkinter import Canvas, Label, NW
from PIL import Image, ImageTk


class Cell:
    def __init__(self, image_location: str = '', x: int = 0, y: int = 0):
        self.image_location = image_location
        self.x, self.y = x, y

    def draw_cell(self, canvas):
        canvas.create_image(self.x, self.y, image=self.image_location, anchor=NW)

    # def open_image(self):
    #     image = Image.open(self.image_location)
    #     image.resize((50, 50), Image.ANTIALIAS)
    #     self.opened_image = ImageTk.PhotoImage(image)
    #
    # def initialise_image_label(self):
    #     image_label = Label(self.application, image=self.opened_image)
    #     image_label.image = self.opened_image
    #     image_label.place(x=self.x, y=self.y)
    #     image_label.pack()
