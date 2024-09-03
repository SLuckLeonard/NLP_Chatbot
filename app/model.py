import random
import spacy

nlp = spacy.load('en_core_web_sm')

# Example responses based on detected intents
RESPONSES = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"]
}


def predict_intent(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ['hello', 'hi'] for token in doc):
        intent = "greeting"
    elif any(token.lemma_ in ['bye', 'goodbye'] for token in doc):
        intent = "goodbye"
    elif any(token.lemma_ in ['thank', 'thanks'] for token in doc):
        intent = "thanks"
    else:
        intent = "unknown"

    return random.choice(RESPONSES.get(intent, ["I don't understand."]))
