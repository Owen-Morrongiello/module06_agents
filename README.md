# README.md
# Author: Owen Morrongiello

## Mini-Project: Gym Class Scheduler
This project simulates a customer service chatbot for a local gym. It uses a `GymLookup` tool to check hardcoded class times from a dictionary, which makes it a "mock" application since it doesn't pull from a real live database. It is designed to hand off conversations to a human if the user mentions words like "billing" or "cancel", as financial transactions are too high-risk for a simple rule-based bot to handle. A major data privacy risk is that if users input their actual credit card numbers or personal addresses into the chat log, the bot's history array stores that sensitive text locally without encryption.


## Week 11 Update: Local AI Integration

For this week I added the local Granite model to my gym chatbot so it could handle random questions from users. One question the model answered really well was about where the gym is located, since it pulled that right from my instructions. One question it refused to answer was when I asked about something random like the weather, and it just gave the default apology message. I decided to keep the class schedule search and the billing transfer rules in regular Python code instead of giving them to the AI. I did this because I do not want the bot to make up fake class times or try to handle sensitive money stuff on its own.

