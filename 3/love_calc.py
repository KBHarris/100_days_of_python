print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is thier name? \n")

combined = name1 + name2

num1 = 0
num2 = 0

num_t = combined.lower().count('t')
num_r = combined.lower().count('r')
num_u = combined.lower().count('u')
num_e = combined.lower().count('e')

num1 = num_t + num_r + num_u + num_e

num2_l = combined.lower().count('l')
num2_o = combined.lower().count('o')
num2_v = combined.lower().count('v')
num2_e = combined.lower().count('e')

num2 = num2_l + num2_o + num2_v + num2_e

score = ((num1 *10) + num2)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

