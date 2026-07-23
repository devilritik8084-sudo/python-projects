
# AI Chatbot V3 Pro Starter
import datetime, random, string, os, time

NOTES="notes.txt"
TODO="todo.txt"

def gen_password(n=12):
    chars=string.ascii_letters+string.digits+"!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(n))

def save_line(file,msg):
    with open(file,"a",encoding="utf-8") as f:
        f.write(msg+"\n")

print("="*50)
print("AI CHATBOT V3 PRO")
print("="*50)
name=input("Enter your name: ")

while True:
    user=input(f"\n{name}: ").strip().lower()

    if user in ["hello","hi","hey","kya ho","kaise ho"]:
        print("Bot: Hello! 😊")
    elif user in ["how are you","how are u"]:
        print("Bot: I'm doing great!")
    elif user in ["your name","who are you"]:
        print("Bot: I am AI Chatbot V3 Pro.")
    elif user in ["who made you","developer"]:
        print("Bot: I was created by Ritik Kumar using Python.")
    elif user in ["python","python info","what is python"]:
        print("Bot: Python is a beginner-friendly programming language.")
    elif user in ["ai","ai info","what is ai"]:
        print("Bot: AI stands for Artificial Intelligence.")
    elif user=="time":
        print(datetime.datetime.now().strftime("%I:%M:%S %p"))
    elif user=="date":
        print(datetime.date.today())
    elif user=="joke":
        print(random.choice(["Programmers love dark mode!","Python improves every day."]))
    elif user=="fact":
        print(random.choice(["GitHub hosts code.","AI learns from data."]))
    elif user=="password":
        print(gen_password(int(input("Length: "))))
    elif user=="calculator":
        a=float(input("First: "))
        op=input("Operator (+,-,*,/): ")
        b=float(input("Second: "))
        print({"+" : a+b, "-" : a-b, "*" : a*b}.get(op, "Cannot divide by zero" if op=="/" and b==0 else a/b if op=="/" else "Invalid"))
    elif user=="note add":
        save_line(NOTES,input("Note: "))
        print("Saved.")
    elif user=="note view":
        print(open(NOTES,encoding="utf-8").read() if os.path.exists(NOTES) else "No notes.")
    elif user=="task add":
        save_line(TODO,input("Task: "))
        print("Saved.")
    elif user=="task view":
        print(open(TODO,encoding="utf-8").read() if os.path.exists(TODO) else "No tasks.")
    elif user=="help":
        print("hello, hi, kya ho, how are you, python info, ai info, time, date, joke, fact, calculator, password, note add, note view, task add, task view, exit")
    elif user=="exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Type 'help'.")
