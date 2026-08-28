# Basic Chatbot - Django + Python

A beginner-friendly rule-based chatbot built with Python and Django.

## Features
- Rule-based responses using `if/elif`
- HTML/CSS chat interface
- Supports hello, hi, how are you, name, thank you, help, and bye
- Default response for unknown messages
- No database or external API required

## Run on Windows

1. Open Command Prompt or PowerShell.
2. Go into the project folder.
3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate it:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the server:

```bash
python manage.py runserver
```

7. Open:

http://127.0.0.1:8000/

## Example messages
- hello
- hi
- how are you
- what is your name
- thank you
- help
- bye

## Project structure

basic_chatbot_django/
├── manage.py
├── requirements.txt
├── README.md
├── chatbot/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── chat/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── chat/
            └── chat.html
