# my_main.py
# Author: Owen Morrongiello

from my_assistant import GymBot
from my_tool import GymLookup

# Set up the fake database and tools
schedule = {"muay thai": "6:00 PM", "boxing": "7:30 PM"}
gym_tool = GymLookup(schedule)
bot = GymBot("Flex", gym_tool)

# Run a quick simulation
print("User: When is the muay thai class?")
print("Bot:", bot.respond("When is the muay thai class?"))

print("\nUser: I need to cancel my membership.")
print("Bot:", bot.respond("I need to cancel my membership."))
