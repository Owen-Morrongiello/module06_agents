# test_my_assistant.py

from mock_model import MockModel
from my_assistant import GymBot
from my_tool import GymLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_bot():
    """Helper to create a fresh bot for testing."""
    schedule = {"muay thai": "6:00 PM", "boxing": "7:30 PM"}
    tool = GymLookup(schedule)
    return GymBot("Flex", "Be helpful.", tool, MockModel())


def make_bot_with_silent_model():
    """Build a GymBot whose model never answers."""
    gym_tool = GymLookup({"muay thai": "6:00 PM", "boxing": "7:00 PM"})
    return GymBot("CoastBot", "Be helpful.", gym_tool, SilentModel())


def test_class_time_rule():
    bot = make_bot()
    assert (
        bot.respond("What time is muay thai?")
        == "The muay thai class is scheduled for 6:00 PM."
    )


def test_safe_reply_when_the_model_has_no_answer():
    bot = make_bot_with_silent_model()
    assert "try again" in bot.respond("hello")
