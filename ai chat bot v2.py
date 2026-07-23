import datetime
import random
import string

print("=" * 45)
print("          AI CHATBOT V2")
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

facts = [
    "Python was created by Guido van Rossum.",
    "Artificial Intelligence can learn from data.",
    "South Korea is one of the world's technology leaders.",
    "The first computer programmer was Ada Lovelace.",
    "GitHub is used to host programming projects."
]

while True:

    user = input(f"\n{name}: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you? 😊")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: My name is AI Chatbot V2.")

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

    elif user == "fact":
        print("Bot:", random.choice(facts))

    elif user == "about":
        print("Bot: I am a simple chatbot made in Python.")

    elif user == "python":
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif user == "ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "roll dice":
        print("Bot: 🎲", random.randint(1, 6))

    elif user == "flip coin":
        print("Bot:", random.choice(["Heads", "Tails"]))

    elif user == "password":
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for i in range(10))
        print("Bot:", password)

    elif user == "calculator":

        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose (1-4): ")

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
        print("fact")
        print("about")
        print("python")
        print("ai")
        print("roll dice")
        print("flip coin")
        print("password")
        print("help")
        print("exit")

    elif user == "exit":

        print("\nBot: Goodbye", name + "!")
        print("Bot: Have a Nice Day!")
        break

    else:

        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")