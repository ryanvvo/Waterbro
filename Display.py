import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk

class Display:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Waterbro")
        self._root.geometry("300x200")
        self._label = tk.Label(self._root, text="00:00")
        self._label.pack()

        self._run_button = tk.Button(width=10, text="Start", command = self.run)
        self._run_button.pack()

        self._add_button = tk.Button(width=10, text="+1 minute", command = self.addMinute)
        self._add_button.pack()

        self._sub_button = tk.Button(width = 10, text = "-1 minute", command = self.subMinute)
        self._sub_button.pack()

        self._stop_button = tk.Button(width = 10, text = "Stop", command = self.stop)
        self._stop_button.pack()

        self._max_time = 0
        self._time = 0
        self._running = False

    def addMinute(self):
        self._time += 60
        self._max_time += 60
        self.update()

    def subMinute(self):
        self._time -= 60
        self._max_time -= 60
        self.update()

    def stop(self):
        if self._running:
            self._running = not self._running
        else:
            self._time = 0
            self._max_time = 0
            self.update()

    def update(self):
        self._label.config(text=_timeToStr(self._time))

    def run(self):
        if not self._running:
            self._running = True
            self.timer()

    def timer(self):
        if not self._running:
            return None
        if self._time <= 0:
            self._time = self._max_time
            playsound("drink_water.wav")
        self.update()
        self._time -= .1
        self._root.after(100, self.timer)


    def mainloop(self):
        self._root.mainloop()

def _timeToStr(time):
    time = int(time)
    seconds = time%60
    minutes = time//60
    return f"{minutes:02d}:{seconds:02d}"