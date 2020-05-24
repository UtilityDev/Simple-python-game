#This is the game. Please give me credit if you're gonna share it on twitter or anywhere else. Thank you.

import random

number = random.randint(0, 50000)
#print("Your number is:", number)
print("The correct number is 10000")

correctNumber = 10000

if number == correctNumber:
    print("Yay, you got it right! You got:", number)
else:
    print("Try again. you got:", number)

print("Game by @Utilityyy_")
