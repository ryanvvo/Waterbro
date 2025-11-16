import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk
from WaterLog import WaterLog
from WaterGoal import WaterGoal

class Display:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Waterbro")
        self._root.geometry("200x200")
        self._root.iconbitmap("bottle.ico")

        self._canvas = tk.Canvas(self._root, width = 500, height = 400)
        self._canvas.pack(fill = "both")

        self._image = Image.open("bottle.jpg").resize((200,200))
        self._photo = ImageTk.PhotoImage(self._image)
        self._canvas.create_image(0, 0, image = self._photo, anchor = "nw")

        self._time_label = tk.Label(self._root, text="00:00")
        self._canvas.create_window(100, 50, window=self._time_label)


        self._run_button = tk.Button(width=10, text="Start", command = self.run)
        self._canvas.create_window(100, 75, window=self._run_button)

        self._add_button = tk.Button(width=10, text="+1 minute", command = self.addMinute)
        self._canvas.create_window(100, 100, window=self._add_button)

        self._sub_button = tk.Button(width = 10, text = "-1 minute", command = self.subMinute)
        self._canvas.create_window(100, 125, window=self._sub_button)

        self._stop_button = tk.Button(width = 10, text = "Stop", command = self.stop)
        self._canvas.create_window(100, 150, window=self._stop_button)

        self._log_button = tk.Button(width = 10, text = "Log Water",
                                        command = lambda: self.expand(self._water_log))
        self._canvas.create_window(50, 175, window = self._log_button)

        self._goal_button = tk.Button(width = 10, text = "Water Goal",
                                        command = lambda: self.expand(self._water_goal))
        self._canvas.create_window(150, 175, window = self._goal_button)

        self._water_log = WaterLog(self._root, self._canvas)
        self._water_goal = WaterGoal(self._root, self._canvas, self._water_log)

        self._max_time = 0
        self._time = 0
        self._running = False
        self._current_side = 0

    def addMinute(self):
        """ Adds a minute from the timer. """
        self._time += 60
        self._max_time += 60
        self.update()

    def subMinute(self):
        """ Subtracts a minute from the timer. """
        self._time -= 60
        self._max_time -= 60
        self.update()

    def stop(self):
        """ Stops the timer, erases current time if already stopped. """
        if self._running:
            self._running = not self._running
        else:
            self._time = 0
            self._max_time = 0
            self.update()

    def update(self):
        """ Updates the timer label to current time. """
        self._time_label.config(text=_timeToStr(self._time))

    def run(self):
        """ Runs the timer. """
        if not self._running:
            self._running = True
            self.timer()

    def timer(self):
        """ Timer mechanic. """
        if not self._running:
            return None
        if self._time <= 0:
            self._time = self._max_time
            playsound("drink_water.wav")
        self.update()
        self._time -= .1
        self._root.after(100, self.timer)

    def expand(self, shown):
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

    def mainloop(self):
        """ Mainloop for Tkinter """
        self._root.mainloop()

def _timeToStr(time):
    """ Converts the time integer to a clock string. """
    time = int(time)
    seconds = time%60
    minutes = time//60
    return f"{minutes:02d}:{seconds:02d}"