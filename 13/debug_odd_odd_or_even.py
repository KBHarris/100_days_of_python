number = int(input("Which number do you wnat to check?: "))

#Bug was caused by the if statement using an assignment operator instead of an equivalency operator
if number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")