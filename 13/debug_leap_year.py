#Year was being set to type Str which is incompatible with type int in math operations
year = int(input("Which year do your want to check? : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")