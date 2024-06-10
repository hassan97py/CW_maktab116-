
try:
    user_input = input("Please enter a number: ")
    number = int(user_input)
    print(f"The number you entered is: [{number}]")
except ValueError:
    print("The input you provided is not a valid integer.")
finally:
    print("Thank you for using the program.")
