from django.test import TestCase
from .views import chatbot_response

class ChatbotResponseTests(TestCase):
    def test_greeting(self):
        self.assertEqual(chatbot_response("hello"), "Hi! How can I help you?")

    def test_how_are_you(self):
        self.assertEqual(chatbot_response("how are you"), "I'm fine, thanks!")

    def test_unknown_message(self):
        self.assertEqual(
            chatbot_response("something random"),
            "Sorry, I don't understand that."
        )
