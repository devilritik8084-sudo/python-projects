import math

while True:

    print("\n==============================")
    print("      MY CALCULATOR APP")
    print("==============================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Square")
    print("7. Cube")
    print("8. Power")
    print("9. Modulus")
    print("10. Square Root")
    print("11. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a + b)

    elif choice == 2:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a - b)

    elif choice == 3:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Answer =", a * b)

    elif choice == 4:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))

        if b == 0:
            print("Division by zero is not possible")
        else:
            print("Answer =", a / b)

    elif choice == 5:
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Average =", (a + b) / 2)

    elif choice == 6:
        a = float(input("Enter Number: "))
        print("Square =", a * a)

    elif choice == 7:
        a = float(input("Enter Number: "))
        print("Cube =", a * a * a)

    elif choice == 8:
        a = float(input("Base: "))
        b = float(input("Power: "))
        print("Answer =", a ** b)

    elif choice == 9:
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        print("Remainder =", a % b)

    elif choice == 10:
        a = float(input("Enter Number: "))
        print("Square Root =", math.sqrt(a))

    elif choice == 11:
        print("Thank You For Using My Calculator")
        break

    else:
        print("Invalid Choice")
        