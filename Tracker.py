import time

class Tracker:
    def __init__(self):
        self._time = 0
        self._duration = 0
        self._start = time.perf_counter()

    def setDuration(self, duration):
        self._duration = duration

    def run(self, func):
        """ Runs a loop that calls func everytime. """
        while True:
            elapsed = time.perf_counter() - self._start
            self._time = self._duration - elapsed
            func()
            if self._time <= 0:
                break
            time.sleep(0.05)

    def getTime(self):
        """ Returns the time of the timer. """
        return self._time