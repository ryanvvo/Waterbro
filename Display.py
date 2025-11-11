import tkinter as tk

class Display:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Waterbro")
        self._root.geometry("300x200")

    def mainloop(self):
        self._root.mainloop()
