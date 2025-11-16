import tkinter as tk
class WaterLog:
    ID = 1

    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        """ Water log aspect of WaterBro, meant to log the water drank. """
        self._root = root
        self._canvas = canvas

        self._ids = []
        self._drank_label = tk.Label(self._root, text="0 fluid ounces")
        self._drank_entry = tk.Entry(self._root, width=10)
        self._drank_button = tk.Button(self._root, text="Drink", command=self.log)
        self._undrank_button = tk.Button(self._root, text="Undrink", command=lambda: self.log(False))

        self._drank = 0

    def show(self) -> int:
        """
        Shows the widgets of the water log

        Returns:
            int: the ID of the log to show Display what is currently on the side.
        """
        self._ids.append(self._canvas.create_window(300, 50, window = self._drank_label))
        self._ids.append(self._canvas.create_window(300, 100, window = self._drank_entry))
        self._ids.append(self._canvas.create_window(300, 125, window = self._drank_button))
        self._ids.append(self._canvas.create_window(300, 155, window = self._undrank_button))
        return self.ID

    def hide(self) -> None:
        """ Hides the widgets of the water log. """
        for value in self._ids:
            self._canvas.delete(value)

    def update(self) -> None:
        """ Updates the amount drank to the label. """
        self._drank_label.config(text=f"{self._drank} fluid ounces")

    def getDrank(self) -> int:
        """
        Returns the amount drank.

        Returns:
            int: Amount drank
        """
        return self._drank

    def log(self, inc = True) -> None:
        """
        Logs the amount of water inputted in the entry, deleting if it is invalid.
        Then, updates the label.
        """
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


