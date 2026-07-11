import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime

# CSV File Read
df = pd.read_csv("patients.csv")

# Features and Target
X = df[["Fever", "Cough", "Headache", "BodyPain"]]
y = df["Disease"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

while True:
    print("\n==============================")
    print(" AI DISEASE PREDICTION SYSTEM ")
    print("==============================")
    print("1. Predict Disease")
    print("2. View Prediction History")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        fever = int(input("Fever (1=Yes,0=No): "))
        cough = int(input("Cough (1=Yes,0=No): "))
        headache = int(input("Headache (1=Yes,0=No): "))
        bodypain = int(input("Body Pain (1=Yes,0=No): "))

        prediction = model.predict([[fever, cough, headache, bodypain]])

        print("\nPredicted Disease:", prediction[0])

        with open("prediction_history.txt", "a") as file:
            file.write(
                f"{datetime.now()} | "
                f"Fever={fever}, Cough={cough}, "
                f"Headache={headache}, BodyPain={bodypain} "
                f"-> {prediction[0]}\n"
            )

        print("Prediction Saved Successfully!")

    elif choice == "2":
        try:
            with open("prediction_history.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No Prediction History Found!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")