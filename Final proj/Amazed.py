import json

def simple_chatbot():
    with open("data.json") as f:
        data = json.load(f)

    print("Hi I am chatbot. Type 'bye' to leave")

    while True:
        user_input = input("You: ").lower()
        if user_input in data:
            print("Bot:", data[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I don't understand that yet.")

simple_chatbot()
