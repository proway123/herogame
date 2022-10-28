from tkinter import Canvas, PhotoImage
from classes.cell import Cell
from PIL import ImageTk

class GameAdmin:

    def __init__(self, application, x, y):
        self.application = application
        self.x = x
        self.y = y

        self.canvas = Canvas(master=application, height=x, width=y)

        self.application.hero_down = ImageTk.PhotoImage(file='images/hero-down.png')
        self.application.hero_up = ImageTk.PhotoImage(file='images/hero-up.png')
        self.application.hero_left = ImageTk.PhotoImage(file='images/hero-left.png')
        self.application.hero_tight = ImageTk.PhotoImage(file='images/hero-right.png')

        self.application.boss = ImageTk.PhotoImage(file='images/boss.png')
        self.application.skeleton = ImageTk.PhotoImage(file='images/skeleton.png')

        self.application.floor = ImageTk.PhotoImage(file='images/floor.png')
        self.application.wall = ImageTk.PhotoImage(file='images/wall.png')


    def draw_map(self):
        for x in range(0, 10):
            for y in range(0, 10):
                cell = Cell(self.application.floor, 10, 10)
                cell.draw_cell(self.canvas)
        self.canvas.pack()





