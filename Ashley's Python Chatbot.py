# Ashley's Python Chatbot

import random
from transformers import pipeline
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download("wordnet")
nltk.download("punkt")

# Load a pre-trained NLP model
chatbot_pipeline = pipeline("text-generation", model="gpt2")

class AdvancedChatbot:
    def __init__(self):
        self.greetings = ["Hello! How can I assist you today?", 
                          "Hi there! What can I help you with?", 
                          "Hello! Feel free to ask me anything."]
        self.farewells = ["Goodbye! Have a great day.", 
                          "Bye! Take care.", 
                          "Farewell!"]

    def get_synonym(self, word):
        # Retrieve synonyms for a word to help expand responses
        synonyms = wordnet.synsets(word)
        return [lemma.name() for synonym in synonyms for lemma in synonym.lemmas()]

    def greet_user(self):
        return random.choice(self.greetings)

    def farewell_user(self):
        return random.choice(self.farewells)

    def generate_response(self, user_input):
        # Tokenize and analyze input
        tokens = word_tokenize(user_input.lower())
        
        # Sample small talk response if greetings are detected
        if any(token in tokens for token in ["hello", "hi", "hey"]):
            return self.greet_user()
        
        # Farewell response if farewells are detected
        if any(token in tokens for token in ["bye", "goodbye", "see you"]):
            return self.farewell_user()
        
        # Generate a conversational response using the NLP model
        response = chatbot_pipeline(user_input, max_length=50, num_return_sequences=1)
        return response[0]["generated_text"]

    def handle_unknown(self):
        responses = ["I'm not sure I understand. Could you rephrase?", 
                     "Could you provide more context?", 
                     "I'm still learning. Could you clarify that?"]
        return random.choice(responses)

# Example of running the chatbot
chatbot = AdvancedChatbot()

# Chat loop
print("Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot:", chatbot.farewell_user())
        break
    
    response = chatbot.generate_response(user_input)
    print("Chatbot:", response if response else chatbot.handle_unknown())