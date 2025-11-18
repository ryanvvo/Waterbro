import json
import os
from datetime import datetime

PATH = "water_save.json"

class WaterSave:
    def __init__(self):
        """
        Saves the water log and goal to a file to be used to save information between sessions.
        """
        self._data = _load_data()
        self.logTime()

    def getDrank(self) -> int:
        """
        Loads the drank information from the file.

        Returns:
            int: amount drank in JSON
        """
        return self._data["drank"]

    def getGoal(self) -> int:
        """
        Loads the goal information from the file.

        Returns:
            int: Goal amount in JSON
        """
        return self._data["goal"]

    def logDrank(self, drank: int) -> None:
        """
        Logs the water drank to the file.

        Args:
            drank (int): The amount drank from WaterLog.
        """
        self._data["drank"] = drank
        with open(PATH, 'w') as file:
            json.dump(self._data, file)

    def logGoal(self, goal: int) -> None:
        """
        Logs the water goal to the file.

        Args:
            goal (int): The goal amount from WaterGoal.
        """
        self._data["goal"] = goal
        with open(PATH, 'w') as file:
            json.dump(self._data, file)

    def logTime(self)  -> None:
        """ Logs the current time to the data. If the time is a different day, reset drank."""
        logged_time = self._data["date"]
        new_time = datetime.now().strftime("%Y-%m-%d")
        if logged_time != new_time:
            self._data["drank"] = 0
        self._data["date"] = new_time

def _load_data() -> dict:
    """
    Loads the data from PATH variable.

    returns:
        dict: Dictionary that holds the data.
    """
    if os.path.exists(PATH):
        with open(PATH, 'r') as file:
            return json.load(file)
    return {"date":datetime.now().strftime("%Y-%m-%d"), "drank":0, "goal":0}
