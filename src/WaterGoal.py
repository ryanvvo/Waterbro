import tkinter as tk
from WaterLog import WaterLog

class WaterGoal:
    ID = 2

    def __init__(self, root: tk.Tk, canvas: tk.Canvas, log: WaterLog, goal: int):
        """
        Water goal aspect of Display, meant to find a target goal and how much remaining.

        Args:
            root (tk.Tk): The root of the GUI.
            canvas (tk.Canvas): The canvas to place the widgets.
            log (WaterLog): WaterLog to measure remaining water left from drank.
            goal (int): Goal from loaded data.
        """
        self._root = root
        self._canvas = canvas
        self._log = log
        self._goal = goal

        self._ids = []
        self._goal_label = tk.Label(self._root)
        self.update()
        self._goal_entry = tk.Entry(self._root, width=10)
        self._calculate_button = tk.Button(self._root, width=10, text="Calculate",
                                           command=self.calculate)

    def show(self) -> int:
        """
        Shows the widgets of Water goal.

        Returns:
            int: ID of WaterGoal to show display what is currently on the side.
        """
        self._ids.append(self._canvas.create_window(300, 50, window = self._goal_label))
        self._ids.append(self._canvas.create_window(300, 125, window = self._goal_entry))
        self._ids.append(self._canvas.create_window(300, 150, window = self._calculate_button))
        return self.ID

    def hide(self) -> None:
        """ Hides all the widgets of Water goal. """
        for value in self._ids:
            self._canvas.delete(value)

    def update(self) -> None:
        """
        Updates the label to show the current goal, how much water is remaining,
        and prompt for entry.
        """
        self._goal_label.config(text=f"Goal: {self._goal} fluid ounces\n"
                                     f"Remaining: {self._goal - self._log.getDrank()} fluid ounces\n"
                                     f"Weight in pounds:")

    def getGoal(self) -> int:
        """
        Returns the goal amount.

        Returns:
            int: Goal amount
        """
        return self._goal

    def calculate(self) -> None:
        """ Calculates the recommended water given pounds, with formula n*.75*.8. """
        try:
            amt = int(self._goal_entry.get())
        except ValueError:
            amt = 0
            self._goal_entry.delete(0, tk.END)

        self._goal = amt * .75 * .8 # 75% of pound to water, 80% of water comes from drinks
        self.update()


