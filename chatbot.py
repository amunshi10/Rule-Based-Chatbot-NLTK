"""Rule-based chatbot core: regex pattern matching + reflections via NLTK's Chat engine."""

from nltk.chat.util import Chat, reflections

custom_reflections = {
    **reflections,
    "am": "are",
    "was": "were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you're": "I am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you",
}

pairs = [
    [
        r"(hi|hello|hey|hola|greetings)[\s\S]*",
        [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Ask me anything.",
        ],
    ],
    [
        r"my name is (.*)",
        [
            "Nice to meet you, %1! How can I help you today?",
            "Hello, %1! What can I do for you?",
        ],
    ],
    [
        r"what(?:'s| is) your name\??",
        ["I'm a rule-based chatbot built with Python and NLTK. You can call me RegexBot!"],
    ],
    [
        r"(who are you|what are you)\??",
        [
            "I'm a simple chatbot that matches your messages against patterns using regular expressions.",
        ],
    ],
    [
        r"how are you\??",
        ["I'm just a program, but I'm running smoothly! How about you?"],
    ],
    [
        r"i am (.*)",
        ["Why do you say you are %1?", "How does being %1 make you feel?"],
    ],
    [
        r"i feel (.*)",
        ["I'm sorry to hear you feel %1. Want to talk about it?", "Why do you feel %1?"],
    ],
    [
        r"(.*) weather (.*)",
        [
            "I can't check live weather, but I hear regex forecasts are always 100%% accurate!",
        ],
    ],
    [
        r"(.*)(joke|funny)(.*)",
        [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I told my computer I needed a break, and now it won't stop sending me KitKats.",
        ],
    ],
    [
        r"(.*)(help|assist|support)(.*)",
        [
            "I can chat about how you're feeling, tell a joke, or just talk. Try saying 'tell me a joke'.",
        ],
    ],
    [
        r"(thank you|thanks)[\s\S]*",
        ["You're welcome!", "Anytime!", "Glad I could help."],
    ],
    [
        r"(bye|goodbye|see you|quit|exit)[\s\S]*",
        ["Goodbye! Have a great day.", "See you later!", "Bye! Come back anytime."],
    ],
    [
        r"quit",
        ["Goodbye!"],
    ],
    [
        r"(.*)",
        [
            "Interesting, tell me more.",
            "I'm not quite sure I understand — could you rephrase that?",
            "Can you elaborate on that?",
        ],
    ],
]


def get_bot():
    return Chat(pairs, custom_reflections)


def get_response(user_input: str) -> str:
    bot = get_bot()
    return bot.respond(user_input) or "I'm not sure how to respond to that."


if __name__ == "__main__":
    bot = get_bot()
    print("RegexBot: Hi! Type 'quit' to exit.")
    bot.converse()
