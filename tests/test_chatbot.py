import unittest
from app.model import predict_intent

class TestChatbot(unittest.TestCase):
    def test_greeting(self):
        response = predict_intent("Hello!")
        self.assertIn(response, ["Hello!", "Hi there!", "Greetings!"])

    def test_goodbye(self):
        response = predict_intent("Goodbye!")
        self.assertIn(response, ["Goodbye!", "See you later!", "Take care!"])

    def test_thanks(self):
        response = predict_intent("Thanks!")
        self.assertIn(response, ["You're welcome!", "No problem!", "Happy to help!"])

if __name__ == '__main__':
    unittest.main()
