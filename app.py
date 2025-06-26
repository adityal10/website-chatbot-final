from interface import Chatbot

if __name__ == "__main__":
    bot = Chatbot()
    print("Jaaji Chatbot is ready (type 'exit' to quit):")
    while True:
        q = input("You: ")
        if q.strip().lower() in {"exit", "quit"}:
            break
        print("Bot:", bot.ask(q))