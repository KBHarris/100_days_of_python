import random

names = input("Give me everyone's names, seperated by a comma. ")

name_list = names.split(",")

x = len(name_list)

chosen = name_list[random.randint(0, (x-1))]

print(f"{chosen} will be paying the bill today!")

