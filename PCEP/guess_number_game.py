"""Making my own number guessing game"""
import random
rand_num = random.randint(1, 101)
# print(rand_num) # Used to trouble shoot the program
target_number = rand_num

# Game Logo
print('''
==========================
=== Secret Number Game ===
==========================
''')

my_guess = 0

while my_guess != target_number:
    my_guess = int(input('Please enter a number between 1 and 100: '))
    if my_guess > target_number:
        print("That number is too high, please try again")
    elif my_guess < target_number:
        print('That number is too low, please try again.')
    else:
        print(f'{target_number} is the correct number')
