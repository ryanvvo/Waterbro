import Display
from Tracker import Tracker

if __name__ == "__main__":
        tracker = Tracker(10)
        tracker.run(lambda: print(tracker.getTime()))
