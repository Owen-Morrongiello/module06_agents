# my_assistant.py
# Author: Owen Morrongiello

HANDOFF_WORDS = ["billing", "cancel", "payment"]


class GymBot:
    def __init__(self, name, gym_tool):
        """Set up the bot with a name, tool, and chat history."""
        self.name = name
        self.gym_tool = gym_tool
        self.history = []

    def respond(self, user_message):
        """Record the message, pick a reply, record the reply, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Mock logic to decide how to answer."""
        text = user_message.lower()

        # Check for human handoff first
        for word in HANDOFF_WORDS:
            if word in text:
                return "I can't handle billing. Let me transfer you to the front desk."

        # Check if they are asking about a class
        if "class" in text or "time" in text:
            class_name = self.gym_tool.find_class(text)
            if class_name is None:
                return "Which class time did you want to check?"

            time = self.gym_tool.get_time(class_name)
            return f"The {class_name} class is scheduled for {time}."

        # Default fallback
        return f"Hi, I'm {self.name}. I can look up class times for you."
