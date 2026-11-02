# README.md
# Author: Owen Morrongiello

## Mini-Project: Gym Class Scheduler
This project simulates a customer service chatbot for a local gym. It uses a `GymLookup` tool to check hardcoded class times from a dictionary, which makes it a "mock" application since it doesn't pull from a real live database. It is designed to hand off conversations to a human if the user mentions words like "billing" or "cancel", as financial transactions are too high-risk for a simple rule-based bot to handle. A major data privacy risk is that if users input their actual credit card numbers or personal addresses into the chat log, the bot's history array stores that sensitive text locally without encryption.
