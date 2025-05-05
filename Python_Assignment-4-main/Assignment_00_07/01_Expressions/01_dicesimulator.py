"""
Program: Dice Simulator
-----------------------
This program rolls two dice three times.
It shows the result of each roll and their total.
Also, it helps explain how variable scope works.
"""

import random  
NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)  
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")

# Main part of the program
def main():
    die1 = 10  
    print(f"die1 in main() starts as: {die1}")

    # Roll the dice three times
    for _ in range(3):
        roll_dice()

    print(f"die1 in main() is still: {die1}")  # Value doesn't change

main()
