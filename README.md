# 🤖 Ashley’s Python Chatbot

Ashley’s Python Chatbot is a smart conversational assistant that blends GPT-2 natural language generation with basic small talk handling and synonym support. Now featuring a polished Tkinter-based GUI, this chatbot provides a more interactive and user-friendly experience, right from your desktop.

---

## ✨ Features

- 🧠 GPT-2 Powered: Uses Hugging Face Transformers to generate intelligent responses.
- 💬 Rule-Based Small Talk: Recognizes greetings and farewells.
- 🔄 Synonym Expansion: WordNet-powered synonym lookup for future expansion.
- 📜 Conversation History Tracking: Maintains a short memory window to generate more relevant responses.
-  Tkinter GUI: Intuitive interface for chatting with the bot.
- 🧪 Fallback Responses: Handles unclear inputs gracefully.

## 📸 GUI Preview

---------------------------------------------
| You: Hello                                |
| Bot: Hello! How can I assist you today?   |
| You: Tell me something cool               |
| Bot: Sure! Here's something interesting...|
---------------------------------------------

## 🚀 Getting Started
✅ Requirements
Python 3.7+

Hugging Face Transformers

NLTK

Tkinter (comes with most Python installations)

Install dependencies with:

pip install transformers nltk

Download NLTK resources:

import nltk
nltk.download("punkt")
nltk.download("wordnet")

## ▶️ Running the Chatbot
To launch the graphical chatbot:

python Ashleys_Python_Chatbot.py

The chatbot will open in a window where you can type and send messages.

## 📁 Project Structure

Ashleys_Python_Chatbot/

├── Ashleys_Python_Chatbot.py     # Main script with chatbot + GUI

├── README.md                     # This file


## 🧠 Behind the Scenes
The chatbot uses GPT-2 via the pipeline("text-generation") method.

A short context window (conversation_history[-5:]) feeds recent dialogue to the model.

Basic greeting and farewell detection is handled using token checks.

Synonym lookup (currently not integrated in generation) uses WordNet and is a hook for future NLP improvements.

## 🔒 License
MIT License. Free for personal and commercial use.

## 🙌 Contributing
Ideas, suggestions, and pull requests are welcome. Feel free to fork this project and make it your own!

