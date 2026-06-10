import streamlit as st

st.title("🤖 Rule-Based AI Chatbot")

user_input = st.text_input("You:")

responses = {
    "hello": "Hi! How are you?",
    "hi": "Hello!",
    "how are you": "I am fine!",
    "what is your name": "I am AI Chatbot",
    "bye": "Goodbye!"
}

if user_input:
    reply = responses.get(
        user_input.lower(),
        "Sorry, I don't understand that."
    )

    st.success(reply)