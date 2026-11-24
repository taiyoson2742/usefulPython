#written 11.23.26
#Must have tkinter installed on your machine

from tkinter import *
from tkinter import ttk
class Sketchpad (Canvas):
    def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            self.bind("<Button-1>", self.set_coord)
            self.bind("<B1-Motion>", self.add_line)
            self.color = 'black'
            self.make_panel()
    def set_coord(self, event):
        self.lastx, self.lasty = event.x, event.y
    def add_line (self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y), fill = self.color)
        self.set_coord (event)
    def set_color(self, newcolor):
        self.color = newcolor
    def make_panel (self):
        idl = self.create_rectangle ((10, 10, 30, 30), fill="red")
        self.tag_bind(idl, "<Button-1>", lambda x: self.set_color("red"))
        id2 = self.create_rectangle((10, 35, 30, 55), fill="blue")
        self.tag_bind(id2, "<Button-1>", lambda x: self.set_color("blue"))
        id3 = self.create_rectangle ((10, 60, 30, 80), fill="black")
        self.tag_bind(id3, "<Button-1>", lambda x: self.set_color("black"))
        id4 = self.create_rectangle((10, 85, 30, 105), fill="green")
        self.tag_bind(id3, "<Button-1>", lambda x: self.set_color("green"))
root = Tk()
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
sketch = Sketchpad(root)
sketch.grid(column=0, row=0, sticky = (N, W, E, S))

root.mainloop()
