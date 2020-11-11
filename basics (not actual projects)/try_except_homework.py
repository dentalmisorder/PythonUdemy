#write a func that asks for int and prints sqrt
import math


def square_of():
    while True:
        user_input = input("Gimme a num to get a square of it: ")
        try:
            x = math.sqrt(int(user_input))
        except:
            print('whoops looks like u arent giving a correct number')
            continue
        else:
            print('all good, square root of {0} is: {1}'.format(user_input, x))
            break

square_of()