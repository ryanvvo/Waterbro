import tkinter as tk
class WaterLog:
    def __init__(self, root, canvas):
        self._root = root
        self._canvas = canvas

        self._ids = []
        self._drank_label = tk.Label(self._root, text="0 fluid ounces")
        self._drank_entry = tk.Entry(self._root, width=10)
        self._drank_button = tk.Button(self._root, text="Drink", command=self.log)
        self._undrank_button = tk.Button(self._root, text="Undrink", command=lambda: self.log(False))

        self._drank = 0

    def show(self):
        self._ids.append(self._canvas.create_window(300, 50, window = self._drank_label))
        self._ids.append(self._canvas.create_window(300, 100, window = self._drank_entry))
        self._ids.append(self._canvas.create_window(300, 125, window = self._drank_button))
        self._ids.append(self._canvas.create_window(300, 155, window = self._undrank_button))

    def hide(self):
        for value in self._ids:
            self._canvas.delete(value)

    def update(self):
        self._drank_label.config(text=f"{self._drank} fluid ounces")

    def log(self, inc = True):
        try:
            amt = int(self._drank_entry.get())
        except ValueError:
            amt = 0
            self._drank_entry.delete(0, tk.END)
        if not inc:
            amt *= -1

        self._drank += amt
        if self._drank < 0:
            self._drank = 0

        self.update()


