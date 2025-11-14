import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk

class Display:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Waterbro")
        self._root.geometry("200x200")

        self._canvas = tk.Canvas(self._root, width = 500, height = 400)
        self._canvas.pack(fill = "both")

        self._image = Image.open("bottle.jpg").resize((200,200))
        self._photo = ImageTk.PhotoImage(self._image)
        self._canvas.create_image(0, 0, image = self._photo, anchor = "nw")

        self._label = tk.Label(self._root, text="00:00")
        self._canvas.create_window(100, 50, window=self._label)


        self._run_button = tk.Button(width=10, text="Start", command = self.run)
        self._canvas.create_window(100, 75, window=self._run_button)

        self._add_button = tk.Button(width=10, text="+1 minute", command = self.addMinute)
        self._canvas.create_window(100, 100, window=self._add_button)

        self._sub_button = tk.Button(width = 10, text = "-1 minute", command = self.subMinute)
        self._canvas.create_window(100, 125, window=self._sub_button)

        self._stop_button = tk.Button(width = 10, text = "Stop", command = self.stop)
        self._canvas.create_window(100, 150, window=self._stop_button)

        self._max_time = 0
        self._time = 0
        self._running = False

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
        self._label.config(text=_timeToStr(self._time))

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


    def mainloop(self):
        """ Mainloop for Tkinter """
        self._root.mainloop()

def _timeToStr(time):
    """ Converts the time integer to a clock string. """
    time = int(time)
    seconds = time%60
    minutes = time//60
    return f"{minutes:02d}:{seconds:02d}"