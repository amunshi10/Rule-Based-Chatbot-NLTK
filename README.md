# RegexBot — Rule-Based Chatbot (Python, NLTK, Regex, Streamlit)

A rule-based chatbot that simulates human-like conversation using pattern matching
instead of machine learning. Built with Python and NLTK, deployed as an interactive
web app with Streamlit.

**Live demo:** https://rule-based-chatbot-nltk-ttaboeb6burusqqcarcjak.streamlit.app/

## What this is

- A conversational agent that matches user input against a set of **regular
  expression patterns** and returns a corresponding response.
- Custom **query-response pairs** covering greetings, small talk, jokes, and a
  fallback for unmatched input.
- **Reflections** (e.g. "I am" → "you are", "my" → "your") so replies read
  naturally instead of just echoing the user's phrasing back.
- No training data, no model weights — every response is deterministic and
  traceable to the rule that produced it.

## How it works

The core logic lives in [`chatbot.py`](chatbot.py) and uses NLTK's
[`nltk.chat.util.Chat`](https://www.nltk.org/api/nltk.chat.util.html) engine:

1. `pairs` is a list of `(regex pattern, [possible responses])` tuples. The first
   pattern that matches the user's input is used; `%1`, `%2`, etc. in a response
   are substituted with the matched groups from the pattern.
2. `reflections` is a dictionary NLTK uses to swap pronouns/verb forms when a
   matched group is echoed back (e.g. user says "I am tired" → bot can say
   "How does being tired make you feel?"). The default NLTK reflections are
   extended with a few extra mappings in `custom_reflections`.
3. If no pattern matches, a catch-all `(.*)` rule at the end returns a generic
   prompt so the bot never fails to respond.

[`app.py`](app.py) wraps this logic in a **Streamlit** chat interface: it keeps
the conversation history in `st.session_state` and re-renders the chat on every
new message.

## Project structure

```
.
├── app.py            # Streamlit UI
├── chatbot.py         # Chat pairs, reflections, and response logic (also runnable in terminal)
├── requirements.txt
└── README.md
```

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

This opens the chat UI in your browser at `http://localhost:8501`.

You can also chat with the bot directly in the terminal without Streamlit:

```bash
python chatbot.py
```

## Deploying to Streamlit Community Cloud

1. Push this repo to GitHub.
2. Sign in at [share.streamlit.io](https://share.streamlit.io) with your GitHub
   account.
3. Click **New app**, select this repository/branch, and set the main file
   path to `app.py`.
4. Deploy — Streamlit installs `requirements.txt` automatically and gives you a
   public URL. Add that URL to the top of this README.

## Tech stack

- **Python**
- **NLTK** (`nltk.chat.util.Chat`) for pattern matching and reflections
- **Regular expressions** for intent patterns
- **Streamlit** for the web UI and hosting
