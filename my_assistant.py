# my_assistant.py
# Author: Owen Morrongiello

HANDOFF_WORDS = ["billing", "cancel", "payment"]

class GymBot:
    def __init__(self, name, instructions, gym_tool, model):
        """Set up the bot with a name, instructions, tool, model, and chat history."""
        self.name = name
        self.instructions = instructions
        self.gym_tool = gym_tool
        self.model = model
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

        # Default fallback goes to the model
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply
