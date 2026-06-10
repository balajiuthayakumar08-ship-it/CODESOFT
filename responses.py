import random

def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there!",
        "how are you": "I'm doing great!",
        "bye": "Goodbye! Have a nice day!",
        "your name": "I am a Rule-Based AI Chatbot.",
        "thanks": "You're welcome!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    jokes = [
        "Why do programmers hate nature? Too many bugs!",
        "Why did Python go to school? To improve its class!",
        "Why was the computer cold? It forgot to close Windows!"
    ]

    if "joke" in user_input:
        return random.choice(jokes)

    return "Sorry, I don't understand that."