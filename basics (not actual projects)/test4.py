#write a function that computes the volume of a sphere given its radius:

def vol(rad):
    return ((4/3) * 3.14) * (rad**3)

print(vol(2))

#write a function that checks whether a number is in a given range (inclusive high n low)

def check_range(num_to_check, min_range, max_range):
    if num_to_check in range(min_range, max_range):
        print('{0} is in the range beetween {1} and {2}'.format(num_to_check, min_range, max_range))
    else:
        print('{0} is NOT in the range beetween {1} and {2}'.format(num_to_check, min_range, max_range))

check_range(3,1,7)
check_range(9,1,7)

#checks how many upper case letters and lower case letters

def up_n_low(text):
    lower_letters=0
    upper_letters=0

    for letter in text:
        if letter.islower() == True:
            lower_letters = lower_letters + 1
        elif letter.isupper() == True:
            upper_letters = upper_letters + 1
    print('In ur text: "{2}"\nLower letters: {0}\nHigher letters: {1}'.format(lower_letters, upper_letters,text))

up_n_low('Hello there Ms. Kitty')

#func that takes a list and returns uniques

def check_unique(list):
    return set(list)

x = check_unique([1,2,1,1,1,1,1,2,2,2,3])
y = check_unique('hello there')

print(list(y))

#func that multiplies all the nums

def multiply(*args):
    return sum(args)

print(multiply(2,2,6,5))

#func that contains all the alphabet atleast once

import string

def is_pangram(text, alphabet=string.ascii_lowercase):
    t_uniq = ''

    for t in text:
        t_uniq = t_uniq + t
    return set(t_uniq) == set(alphabet)
        

print(is_pangram('qwertyuiopadfgdfgdfgdfgrewszzdfghhhhhhjklzxcvbnm'))