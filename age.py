while True:
    try:
        age = int(input("Enter your age:"))
        break
    except ValueError as ve:
        print("Invalid input. Please enter your age again.",ve)

if age % 2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")
