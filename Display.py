import tkinter as tk

class Display:
    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Waterbro")
        self._root.geometry("300x200")
        self._label = tk.Label(self._root, text="00:00")
        self._label.pack()

        self._button = tk.Button()
        self._button.pack()

        self._time = 60

    def update(self):
        self._label.config(text=_timeToStr(self._time))

    def run(self):
        self.update()
        self._time -= .1
        self._root.after(100, self.run)

    def mainloop(self):
        self._root.mainloop()

def _timeToStr(time):
    time = int(time)
    seconds = time%60
    minutes = time//60
    return f"{minutes:02d}:{seconds:02d}"