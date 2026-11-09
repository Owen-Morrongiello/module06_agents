# my_main.py
# Author: Owen Morrongiello

from my_assistant import GymBot
from my_tool import GymLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Flex, a helpful support assistant for Coast Tech Gym.
Answer in one short sentence.
Our facility is located in Tampa, Florida.
Memberships cost $50 per month.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to the front desk."""

# Set up the fake database and tools
schedule = {"muay thai": "6:00 PM", "boxing": "7:30 PM"}
gym_tool = GymLookup(schedule)
model = OllamaModel(MODEL_NAME)

# Set up the bot with instructions, tool, and model
bot = GymBot("Flex", INSTRUCTIONS, gym_tool, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
