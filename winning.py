# WAP for winning number:

import random
n= random.randint(1,100)
num_of_guess= 1
print("number of Guesses is limited to only 5 times ")

while (num_of_guess<= 5):
    guess_num= int(input("guess the number between 1 to 100: "))
    if guess_num < n:
        print("You have enter less number please input greater number.\n")
    elif guess_num > n:
        print("You have enter greater number please input smaller number.\n")
    else:
        print("You won!\n")
        print(num_of_guess,"no. of guesses he took to finish.")
        break
    print(5-num_of_guess,"no. of guesses left")
    num_of_guess += 1

if num_of_guess > 5:
    print("Game Over")
