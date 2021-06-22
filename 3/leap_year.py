year = int(input("Which year do you wnat to check? "))

rule1 = False
rule2 = False
rule3 = False

if year % 4 == 0:
    rule1 = True
if year % 100 == 0:
    rule2 = True
if year % 400 == 0:
    rule3 = True

if rule1 and rule2 and rule3 == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")