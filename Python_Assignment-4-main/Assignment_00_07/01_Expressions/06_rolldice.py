import random
NUM_SIDES = 6

def main():
    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)
    total = dice1 + dice2

    print(f"Dice have {NUM_SIDES} sides each.")     
    print(f"First dice = {dice1}")
    print(f"Second dice = {dice2}")
    print("Total of two dice:", total)

main()
