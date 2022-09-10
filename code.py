import dice
import os


while True:
    user_input = int(input("Enter Number of Dice:"))
    os.system('cls')
    if user_input == 0:
        break
    dice.get_dice(user_input)



