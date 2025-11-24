import tkinter as tk
from tkinter import messagebox
from playsound import playsound
from PIL import Image, ImageTk
from WaterLog import WaterLog
from WaterGoal import WaterGoal
from WaterSave import WaterSave

class Display:
    def __init__(self):
        """ Main display of WaterBro. Does the timer mechanic and GUI aspect. """
        self._root = tk.Tk()
        self._setup_root()

        self._canvas = tk.Canvas(self._root, width = 500, height = 400)
        self._canvas.pack(fill = "both")

        self._image = Image.open("bottle.jpg").resize((200,200))
        self._photo = ImageTk.PhotoImage(self._image)
        self._canvas.create_image(0, 0, image = self._photo, anchor = "nw")

        self._time_label = tk.Label(self._root, text="00:00 / 00:00")
        self._run_button = tk.Button(width=10, text="Start", command = self.run)
        self._add_button = tk.Button(width=10, text="+1 minute", command = self.addMinute)
        self._sub_button = tk.Button(width = 10, text = "-1 minute", command = self.subMinute)
        self._stop_button = tk.Button(width = 10, text = "Stop", command = self.stop)
        self._log_button = tk.Button(width = 10, text = "Log Water",
                                        command = lambda: self.expand(self._water_log))
        self._goal_button = tk.Button(width = 10, text = "Water Goal",
                                        command = lambda: self.expand(self._water_goal))

        self._silent = tk.BooleanVar(value=False)
        self._silent_check = tk.Checkbutton(self._root, text="Silent mode", variable=self._silent,
                                            font=("arial", 8))

        self._water_save = WaterSave()
        self._water_log = WaterLog(self._root, self._canvas, self._water_save.getDrank())
        self._water_goal = WaterGoal(self._root, self._canvas, self._water_log, self._water_save.getGoal())

        self._initialize_canvas_windows()

        self._max_time = self._water_save.getMaxTime()
        self._time = self._max_time
        self._running = False
        self._current_side = 0
        self.update()

    def _setup_root(self):
        """ Sets up the settings for the root. """
        self._root.title("Waterbro")
        self._root.geometry("200x200")
        self._root.iconbitmap("bottle.ico")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.bind_all("<Button-1>", self.checkTime)

    def _initialize_canvas_windows(self) -> None:
        """ Adds all the widgets to the canvas. """
        self._canvas.create_window(100, 50, window=self._time_label)
        self._canvas.create_window(100, 75, window=self._run_button)
        self._canvas.create_window(100, 75, window=self._run_button)
        self._canvas.create_window(100, 100, window=self._add_button)
        self._canvas.create_window(100, 125, window=self._sub_button)
        self._canvas.create_window(100, 150, window=self._stop_button)
        self._canvas.create_window(50, 175, window = self._log_button)
        self._canvas.create_window(150, 175, window = self._goal_button)
        self._canvas.create_window(35, 10, window = self._silent_check)

    def addMinute(self) -> None:
        """ Adds a minute from the timer. """
        self._time += 60
        self._max_time += 60
        self.update()

    def subMinute(self) -> None:
        """ Subtracts a minute from the timer. """
        self._time -= 60
        self._max_time -= 60
        self.update()

    def stop(self) -> None:
        """ Stops the timer; erases current time if already stopped. """
        if self._running:
            self._running = not self._running
        else:
            self._time = 0
            self._max_time = 0
            self.update()

    def update(self) -> None:
        """ Updates the text of the labels. """
        self._time_label.config(text=f"{_timeToStr(self._time)} / {_timeToStr(self._max_time)}")

    def run(self) -> None:
        """ Runs the timer. """
        if not self._running:
            self._running = True
            self.timer()

    def timer(self) -> None:
        """ Timer mechanic. """
        if not self._running:
            return None
        if self._time <= 0:
            self._time = self._max_time
            self._notify()
        self.update()
        self._time -= .1
        self._root.after(100, self.timer)

    def _notify(self) -> None:
        """ Sends an alert depending on whether silent is on or not. """
        if not self._silent.get():
            playsound("drink_water.wav")
        else:
            messagebox.showinfo("DRINK", "TIME TO DRINK")

    def expand(self, shown: WaterLog|WaterGoal) -> None:
        """
        Expands the window to show side information.

        Args:
            shown (WaterLog|WaterGoal): The element that is being shown.
        """
        if self._root.winfo_width() <= 200:
            self._root.geometry("400x200")
            self._current_side = shown.show()
        elif self._current_side == shown.ID:
            self._root.geometry("200x200")
            shown.hide()
        elif self._current_side == WaterLog.ID:
            self._water_log.hide()
            self._water_goal.show()
            self._current_side = WaterGoal.ID
        elif self._current_side == WaterGoal.ID:
            self._water_goal.hide()
            self._water_log.show()
            self._current_side = WaterLog.ID

    def mainloop(self) -> None:
        """ Mainloop for Tkinter """
        self._root.mainloop()

    def close(self) -> None:
        """ Runs events upon closing the root. """
        self._water_save.logDrank(self._water_log.getDrank())
        self._water_save.logGoal(self._water_goal.getGoal())
        self._water_save.logTime()
        self._water_save.logMaxTime(self._max_time)
        self._root.destroy()

    def checkTime(self, event:tk.Event) -> None:
        """ Logs the time every action to track a reset. """
        self._water_save.logTime()


def _timeToStr(time: int) -> str:
    """
    Converts the time integer to a clock string.

    Args:
        time(int): Amount of seconds.

    Returns:
        str: Time in (00:00) format.
    """
    time = int(time)
    seconds = time%60
    minutes = time//60
    return f"{minutes:02d}:{seconds:02d}"