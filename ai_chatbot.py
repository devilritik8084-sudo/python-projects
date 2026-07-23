import datetime
import random

print("=" * 45)
print("          AI CHATBOT V1")
print("=" * 45)

name = input("Enter your name: ")

print(f"\nHello {name}! 😊")
print("I am your AI Chatbot.")
print("Type 'help' to see commands.")
print("Type 'exit' to quit.\n")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to school? To improve its class!",
    "I would tell you a UDP joke, but you might not get it.",
    "Why do Java developers wear glasses? Because they don't C#."
]

while True:

    user = input(f"\n{name}: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you? 😊")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: My name is AI Chatbot V1.")

    elif user == "who made you":
        print("Bot: I was created by Ritik Kumar using Python.")

    elif user == "time":
        now = datetime.datetime.now()
        print("Bot:", now.strftime("%I:%M:%S %p"))

    elif user == "date":
        today = datetime.date.today()
        print("Bot:", today)

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "calculator":

        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose: ")

        if choice == "1":
            a = float(input("First Number: "))
            b = float(input("Second Number: "))
            print("Bot:", a + b)

        elif choice == "2":
            a = float(input("First Number: "))
            b = float(input("Second Number: "))
            print("Bot:", a - b)

        elif choice == "3":
            a = float(input("First Number: "))
            b = float(input("Second Number: "))
            print("Bot:", a * b)

        elif choice == "4":
            a = float(input("First Number: "))
            b = float(input("Second Number: "))

            if b == 0:
                print("Bot: Cannot divide by zero!")
            else:
                print("Bot:", a / b)

        else:
            print("Bot: Invalid Choice!")

    elif user == "help":

        print("\n========== COMMANDS ==========")
        print("hello")
        print("hi")
        print("how are you")
        print("your name")
        print("who made you")
        print("time")
        print("date")
        print("calculator")
        print("joke")
        print("help")
        print("exit")

    elif user == "exit":

        print("\nBot: Goodbye", name + "!")
        print("Bot: Have a Nice Day!")
        break

    else:

        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")