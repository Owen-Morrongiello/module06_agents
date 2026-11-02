# tests/test_my_assistant.py
# Author: Owen Morrongiello

from my_assistant import GymBot
from my_tool import GymLookup


def make_bot():
    """Helper to create a fresh bot for testing."""
    schedule = {"muay thai": "6:00 PM", "boxing": "7:30 PM"}
    tool = GymLookup(schedule)
    return GymBot("Flex", tool)


def test_bot_finds_class_time():
    bot = make_bot()
    reply = bot.respond("What time is the muay thai class?")
    assert "6:00 PM" in reply


def test_bot_hands_off_billing():
    bot = make_bot()
    reply = bot.respond("I need help with my billing.")
    assert "front desk" in reply
