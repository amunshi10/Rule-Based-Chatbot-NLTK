import streamlit as st

from chatbot import get_bot

st.set_page_config(page_title="RegexBot — Rule-Based Chatbot", page_icon="💬")

st.title("💬 RegexBot")
st.caption("A rule-based chatbot built with Python, NLTK, and regular expressions.")

if "bot" not in st.session_state:
    st.session_state.bot = get_bot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm RegexBot. Ask me something or say hello."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    reply = st.session_state.bot.respond(user_input) or "I'm not sure how to respond to that."
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

with st.sidebar:
    st.header("About")
    st.write(
        "This chatbot uses **pattern matching with regular expressions** and "
        "**custom query-response pairs** built on top of NLTK's `Chat` utility, "
        "including reflections (e.g. 'I am' → 'you are') for more natural replies."
    )
    if st.button("Reset conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm RegexBot. Ask me something or say hello."}
        ]
        st.rerun()
