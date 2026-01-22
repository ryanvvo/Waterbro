import tkinter as tk
import WaterTools
import WaterSave
class WaterLog:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas, save: WaterSave):
        """
        Water log aspect of WaterBro, meant to log the water drank.

        Args:
            root (tk.Tk): The root of the GUI.
            canvas (tk.Canvas): The canvas to place the widgets.
            save (WaterSave): Save object.
        """
        self._root = root
        self._canvas = canvas
        self._drank = save.getDrank()

        self._ids = []
        self._drank_label = tk.Label(self._root)
        self._water_save = save
        self.update()
        self._drank_entry = tk.Entry(self._root, width=10)
        self._drank_button = tk.Button(self._root, text="Drink", command=self.log)
        self._undrank_button = tk.Button(self._root, text="Undrink", command=lambda: self.log(False))


    def show(self) -> None:
        """
        Shows the widgets of the water log

        Returns:
            int: the ID of the log to show Display what is currently on the side.
        """
        self._ids.append(self._canvas.create_window(300, 50, window = self._drank_label))
        self._ids.append(self._canvas.create_window(300, 100, window = self._drank_entry))
        self._ids.append(self._canvas.create_window(300, 125, window = self._drank_button))
        self._ids.append(self._canvas.create_window(300, 155, window = self._undrank_button))

    def hide(self) -> None:
        """ Hides the widgets of the water log. """
        for value in self._ids:
            self._canvas.delete(value)

    def update(self) -> None:
        """
        Updates the amount drank to the label.

        Args:
            metric (bool): Boolean that determines whether fluid ounces or liters.
        """
        metric = self._water_save.getSettings()["metric"]
        if metric:
            self._drank_label.config(text = f"{WaterTools.ounce2liter(self._drank)} liters")
        else:
            self._drank_label.config(text = f"{self._drank} fluid ounces")

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

        if self._water_save.getSettings()["metric"]:
            self._drank += WaterTools.liter2ounce(amt)
        else:
            self._drank += amt

        if self._drank < 0:
            self._drank = 0
        self.update()


