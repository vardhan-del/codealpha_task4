from django.shortcuts import render


def chatbot_response(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hi! How can I help you?"

    elif "how are you" in message:
        return "I'm fine, thanks!"

    elif "name" in message:
        return "I'm a simple Python chatbot."

    elif "thank" in message:
        return "You're welcome!"

    elif "help" in message:
        return "Sure! You can say hello, ask how I am, or say bye."

    elif "bye" in message:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


def chat_view(request):
    user_message = ""
    bot_response = ""

    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()

        if user_message:
            bot_response = chatbot_response(user_message)

    return render(
        request,
        "chat/chat.html",
        {
            "user_message": user_message,
            "bot_response": bot_response,
        },
    )
