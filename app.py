import html

import streamlit as st

from chatbot import get_bot

st.set_page_config(page_title="RegexBot — Rule-Based Chatbot", page_icon="💬")

CHAT_CSS = """
<style>
.stApp, .stApp * {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.chat-thread {
    display: flex;
    flex-direction: column;
    padding: 4px 0 12px 0;
}
.msg-row {
    display: flex;
    width: 100%;
}
.msg-row.role-user { justify-content: flex-end; }
.msg-row.role-assistant { justify-content: flex-start; }
.msg-row.gap-tight { margin-top: 8px; }
.msg-row.gap-wide { margin-top: 20px; }
.bubble {
    max-width: 75%;
    padding: 12px 16px;
    border-radius: 20px;
    line-height: 1.5;
    font-size: 0.95rem;
    word-wrap: break-word;
    white-space: pre-wrap;
}
.bubble.role-user {
    background: #4F46E5;
    color: #EDE9FE;
    border-bottom-right-radius: 6px;
}
.bubble.role-assistant {
    background: #EEF1F6;
    color: #1E2333;
    border-bottom-left-radius: 6px;
}
</style>
"""

st.markdown(CHAT_CSS, unsafe_allow_html=True)

st.title("💬 RegexBot")
st.caption("A rule-based chatbot built with Python, NLTK, and regular expressions.")

if "bot" not in st.session_state:
    st.session_state.bot = get_bot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm RegexBot. Ask me something or say hello."}
    ]


def render_thread(messages):
    rows = ['<div class="chat-thread">']
    prev_role = None
    for msg in messages:
        role = msg["role"]
        gap_class = "" if prev_role is None else ("gap-tight" if role == prev_role else "gap-wide")
        text = html.escape(msg["content"]).replace("\n", "<br>")
        rows.append(
            f'<div class="msg-row role-{role} {gap_class}">'
            f'<div class="bubble role-{role}">{text}</div>'
            f"</div>"
        )
        prev_role = role
    rows.append("</div>")
    return "".join(rows)


if user_input := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = st.session_state.bot.respond(user_input) or "I'm not sure how to respond to that."
    st.session_state.messages.append({"role": "assistant", "content": reply})

st.markdown(render_thread(st.session_state.messages), unsafe_allow_html=True)

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
