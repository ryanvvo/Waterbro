import tkinter as tk

class Settings:
    def __init__(self, root: tk.Tk, canvas: tk.Canvas):
        """
        Settings hold user choice of the program.

        Args:
            root (tk.Tk): The root of the GUI.
            canvas (tk.Canvas): The canvas to place the widgets.
        """
        self._root = root
        self._canvas = canvas

        self._ids = []
        self._settings_label = tk.Label(self._root, text="Settings")
        self._apply_button = tk.Button(self._root, width=10, text="Apply",
                                           command=self.apply)
        self._initialize_settings()

    def _initialize_settings(self):
        pass

    def show(self) -> None:
        """
        Shows the available settings.

        Returns:
            int: ID of WaterGoal to show display what is currently on the side.
        """
        self._ids.append(self._canvas.create_window(300, 50, window = self._settings_label))


    def hide(self) -> None:
        """ Hides all the widgets of Water goal. """
        for value in self._ids:
            self._canvas.delete(value)

    def apply(self) -> None:
        """
        Applies the settings.
        """


