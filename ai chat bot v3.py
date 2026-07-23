# AI Chatbot V3
import datetime, random, string, time, os

notes_file="notes.txt"
todo_file="todo.txt"

jokes=["Why do programmers prefer dark mode? Because light attracts bugs!",
"Why did Python go to school? To improve its class!"]
facts=["Python was created by Guido van Rossum.",
"AI enables computers to learn from data.",
"GitHub hosts software projects."]

def password(n=12):
    chars=string.ascii_letters+string.digits+"!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(n))

def add_note():
    t=input("Enter note: ")
    with open(notes_file,"a") as f:f.write(t+"\n")
    print("Saved.")

def view_notes():
    if not os.path.exists(notes_file): print("No notes.");return
    print(open(notes_file).read())

def add_task():
    t=input("Task: ")
    with open(todo_file,"a") as f:f.write(t+"\n")
    print("Added.")

def view_tasks():
    if not os.path.exists(todo_file): print("No tasks.");return
    print(open(todo_file).read())

print("="*45)
print("AI CHATBOT V3")
print("="*45)
name=input("Name: ")

while True:
    cmd=input(f"\n{name}: ").lower()

    if cmd in ("hi","hello"): print("Hello!")
    elif cmd=="time": print(datetime.datetime.now().strftime("%I:%M:%S %p"))
    elif cmd=="date": print(datetime.date.today())
    elif cmd=="joke": print(random.choice(jokes))
    elif cmd=="fact": print(random.choice(facts))
    elif cmd=="python": print("Python is a powerful programming language.")
    elif cmd=="ai": print("AI means Artificial Intelligence.")
    elif cmd=="password":
        print(password(int(input("Length: "))))
    elif cmd=="calculator":
        a=float(input("First: "));op=input("Operator(+,-,*,/): ");b=float(input("Second: "))
        if op=="+": print(a+b)
        elif op=="-": print(a-b)
        elif op=="*": print(a*b)
        elif op=="/": print("Cannot divide by zero" if b==0 else a/b)
    elif cmd=="dice": print(random.randint(1,6))
    elif cmd=="coin": print(random.choice(["Heads","Tails"]))
    elif cmd=="note add": add_note()
    elif cmd=="note view": view_notes()
    elif cmd=="task add": add_task()
    elif cmd=="task view": view_tasks()
    elif cmd=="guess":
        n=random.randint(1,10)
        g=int(input("Guess 1-10: "))
        print("Correct!" if g==n else f"Wrong! Number was {n}")
    elif cmd=="stopwatch":
        s=int(input("Seconds: "))
        while s:
            print(s)
            time.sleep(1)
            s-=1
        print("Done!")
    elif cmd=="help":
        print("hello,time,date,joke,fact,python,ai,password,calculator,dice,coin,note add,note view,task add,task view,guess,stopwatch,exit")
    elif cmd=="exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")
