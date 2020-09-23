#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
#if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        elif num1 > num2:
            return num2
    elif num1 % 2 != 0 or num2 % 2 != 0:
        if num1 < num2:
            return num2
        elif num1 > num2:
            return num1

#ANIMAL CRACKERS: Write a function takes a two-word string and returns 
#True if both words begin with same letter

def animal_crackers(two_words):
    count = 0
    letter_first = ''
    letter_second = ''

    splited_words = two_words.split()
    for word in splited_words:
        if count == 0:
            letter_first = word[0]
        elif count == 1:
            letter_second = word[0]
        count=count +1
    if letter_first == letter_second:
        return True
    else:
        return False

#MAKES TWENTY: Given two integers, return True if the sum 
#of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(num1,num2):
    if sum(num1,num2) == 20 or num1 == 20 or num2 == 20:
        return True
    else:
        return False

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(st):
    new_st=''
    count = 0
    for letter in st:
        if count == 0:
            letter = letter.upper()
        elif count == 3:
            letter = letter.upper()
        count = count + 1
        new_st = new_st + letter
    return new_st

#MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    text_splitted = text.split(' ')
    new_text = []
    for word in text_splitted:
        new_text.insert(0, word)
    new_text = " ".join(new_text)
    print(new_text)

master_yoda('all i want from my life is small tiddie goth gf who i can play animal crossing with')

#ALMOST THERE: Given an integer n, return True
# if n is within 10 of either 100 or 200

def almost_there(num):
    if abs(num) >= 90 and abs(num) <= 110:
        return True
    elif abs(num) >= 190 and abs(num) <= 210: 
        return True
    else:
        return False

#FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_thirty_three(num_list):
    prev_num = 0
    for num in num_list:
        if num == prev_num:
            if prev_num == 3:
                return True
        prev_num = num
    return False