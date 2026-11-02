# my_tool.py
# Author: Owen Morrongiello


class GymLookup:
    def __init__(self, schedule):
        """Store the fake class schedule dictionary."""
        self.schedule = schedule

    def find_class(self, text):
        """Extract the class name from the user's message."""
        text = text.lower()
        if "muay thai" in text:
            return "muay thai"
        if "boxing" in text:
            return "boxing"
        return None

    def get_time(self, class_name):
        """Return the time for the class, or None."""
        if class_name in self.schedule:
            return self.schedule[class_name]
        return None
