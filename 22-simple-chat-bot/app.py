import random
import time

def chatbot():
    greetings = ["Hello there! 👋", "Hi friend! 😊", "Hey! Nice to meet you! 🤝", "Howdy! 😊"]

    farewells = ["Goodbye! 👋", "See you later! 🚶‍♂️", "Bye bye! 🙋‍♂️", "Until next time! 😎"]

    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field! 😂",
        "Why don't scientists trust atoms? Because they make up everything! 🤣",
        "What do you call fake spaghetti? An impasta! 🍝🤣",
        "Why did the bicycle fall over? Because it was two-tired! 🚲😄",
        "What do you call cheese that isn't yours? Nacho cheese! 🧀😆"
    ]

    facts = [
        "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old! 🍯",
        "Bananas are berries, but strawberries aren't! 🍌🍓",
        "Octopuses have three hearts and blue blood! 🐙💙",
        "A group of flamingos is called a 'flamboyance'! 🦩✨",
        "Wombat poop is cube-shaped! 🐾"
    ]

    bot_name = "ChatBot"
    print(f"🤖 {bot_name} is starting up...")
    time.sleep(2)

    print(f"""
        🤖 Welcome to {bot_name}! 🤖

        I can chat about:
        🎯 'joke' - Hear a funny joke
        🧠 'fact' - Learn something new
        🌈 'color' - My favorite color
        👋 'bye' - End our chat
        """)
    
    chatting = True
    user_name = input("What's your name: ").lower().strip()
    print(f"🤖 {bot_name}: Nice to meet you, {user_name}! How can I help you today? 😊")

    while chatting:
        user_input = input("😊 You: ").strip()

        if user_input in ["hi", "hello", "hey", "howdy"]:
            print(f"🤖 {bot_name}: {random.choice(greetings)}")

        elif "joke" in user_input:
            print(f"🤖 {bot_name}: {random.choice(jokes)}")

        elif "fact" in user_input:
            print(f"🤖 {bot_name}: {random.choice(facts)}")

        elif "color" in user_input:
            print(f"🤖 {bot_name}: My favorite color is robot blue! 💙 What's yours?")
            color = input("😊 You: ").strip()
            print(f"🤖 {bot_name}: {color} is a great choice! 🎨")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print(f"🤖 {bot_name}: {random.choice(farewells)}")
            print(f"🤖 {bot_name}: It was fun chatting with you, {user_name}")
            chatting = False

        else:
            responses = [
                "That's interesting! Tell me more! 🤔",
                "I'm not sure I understand. Can you try again? 🤗",
                "Hmm, let's talk about something else. Try asking for a joke or fact!",
                "Beep boop! My rorbot brain is processing that... 🤔"
            ]
            print(f"🤖 {bot_name}: {random.choice(responses)}")

    print("Thanks for chatting! Run the program again to talk to me later! 👋")

chatbot()

    