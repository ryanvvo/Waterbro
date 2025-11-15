import tkinter as tk
class WaterLog:
    def __init__(self, root, canvas):
        self._root = root
        self._canvas = canvas
        self._drank_label = tk.Label(self._root, text="0 fluid ounces")
        self._drank_label_id = 0

    def show(self):
        self._drank_label_id = self._canvas.create_window(300, 50, window = self._drank_label)

    def hide(self):
        self._canvas.delete(self._drank_label_id)