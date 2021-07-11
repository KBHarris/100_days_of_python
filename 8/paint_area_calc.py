import math

def print_calc(height, width, cover):
    num_cans = (height * width) / cover
    total_cans = math.ceil(num_cans)
    print(f"You will need {total_cans} cans.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print_calc(height=test_h, width=test_w, cover=coverage)
