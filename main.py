import random


points = 0

def guess(x):
    global points  
    num = random.randint(1, 5)
    if x == num:
        print("Correct! You guessed the number.")
        points += 10
    else:
        print(f"Wrong! The correct number was {num}.")

def start_game():
    while True:
        try:
            x = int(input("Please enter a number from 1 to 5: "))
            if 1 <= x <= 5:
                return x
            else:
                print("Please enter a number within the range!")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main game loop
a = 0
while a < 5:
    user_guess = start_game()
    guess(user_guess)
    a += 1
else: 
    print(f"You have {points} points.")
