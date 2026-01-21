import tkinter as tk

class Settings:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas, settings: dict):
        """
        Settings hold user choice of the program.

        Args:
            root (tk.Tk): The root of the GUI.
            canvas (tk.Canvas): The canvas to place the widgets.
        """
        self._root = root
        self._canvas = canvas
        self._settings = settings

        self._ids = []
        self._settings_label = tk.Label(self._root, text="Settings")
        self._apply_button = tk.Button(self._root, width=10, text="Apply",
                                           command=self.apply)

        self._initialize_settings()

    def _initialize_settings(self):
        self._silent = tk.BooleanVar(value = self._settings["silent"])
        self._silent_check = tk.Checkbutton(self._root, text = "Silent mode",
                                            variable = self._silent,
                                            font = ("arial", 8))
        self._metric = tk.BooleanVar(value = self._settings["metric"])
        self._metric_check = tk.Checkbutton(self._root, text = "Metric system",
                                            variable = self._metric,
                                            font = ("arial", 8))

    def show(self) -> None:
        """
        Shows the available settings.

        Returns:
            int: ID of WaterGoal to show display what is currently on the side.
        """
        self._ids.append(self._canvas.create_window(300, 50, window = self._settings_label))
        self._ids.append(self._canvas.create_window(300, 110, window = self._apply_button))
        self._ids.append(self._canvas.create_window(300, 70, window = self._silent_check))
        self._ids.append(self._canvas.create_window(300, 90, window = self._metric_check))


    def hide(self) -> None:
        """ Hides all the widgets of Water goal. """
        for value in self._ids:
            self._canvas.delete(value)

    def apply(self) -> None:
        """
        Saves the settings.
        """
        self._settings["silent"] = self._silent.get()
        self._settings["metric"] = self._metric.get()

    def getSettings(self) -> dict:
        """
        Returns the current settings.

        Returns:
            dict: Current settings
        """
        return self._settings

