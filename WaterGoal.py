import tkinter as tk
class WaterGoal:
    ID = 2

    def __init__(self, root, canvas, log):
        self._root = root
        self._canvas = canvas
        self._log = log

        self._ids = []
        self._goal_label = tk.Label(self._root, text="Goal: 0 fluid ounces\n"
                                                     "Remaining: 0 fluid ounces\n"
                                                     "Weight in pounds:")
        self._goal_entry = tk.Entry(self._root, width=10)
        self._calculate_button = tk.Button(self._root, width=10, text="Calculate",
                                           command=self.calculate)

        self._goal = 0

    def show(self):
        self._ids.append(self._canvas.create_window(300, 50, window = self._goal_label))
        self._ids.append(self._canvas.create_window(300, 125, window = self._goal_entry))
        self._ids.append(self._canvas.create_window(300, 150, window = self._calculate_button))
        return self.ID

    def hide(self):
        for value in self._ids:
            self._canvas.delete(value)

    def update(self):
        self._goal_label.config(text=f"Goal: {self._goal} fluid ounces\n"
                                     f"Remaining: {self._goal - self._log.getDrank()} fluid ounces\n"
                                     f"Weight in pounds:")

    def calculate(self):
        try:
            amt = int(self._goal_entry.get())
        except ValueError:
            amt = 0
            self._goal_entry.delete(0, tk.END)

        self._goal = amt * .75 * .8 # 75% of pound to water, 80% of water comes from drinks
        self.update()


