#✿ ❤ ✿ guessing game (угадай число) ✿ ❤ ✿

#import
import random
#import

#style characters
flowers = "✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿"
hearts = "❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤"
#style characters

guess_max = int(input("Set the max num from guessing range: "))
lives_limit = int(input("In how many tries u wanna guess it?: "))
guess_right = random.randint(0, guess_max)
guessed = False
lives = lives_limit

while lives > 0:
    user_input = int(input(f"Guess the number from 0 to {guess_max}: "))
    lives -= 1
    if user_input == guess_right:
        print(f"\n{hearts}\n❤ U guessed it right! It was {guess_right} ❤\n{hearts}\n")
        guessed = True
        break
    elif user_input != guess_right:
        print("bruh dud try one more time")

print(f"\n{flowers}\n✿ Game ended! \n✿ Guessed: {guessed} \n✿ Lives left: {lives}/{lives_limit}\n{flowers}\n")
if user_input != guess_right:
    print(f"Guessed num was {guess_right}")