#second test on Udemy

#print from string only words that start with 's'

st = 'Print only the words that start with s in this sentence'

st_splited = st.split()
print(f'\n{st_splited}') #split them into words in different strings

for word in st_splited:
    if word[0].lower() == 's': #check if it starts with 's', using lower to check in upper case too
        print(word)

#use range and print even nums from 0 to 10

for num in range(0,11):
    if num % 2 == 0:
        print(num)

#use list comprehension to create a list of all nums between 1 and 50 that are divisible by 3

my_list = []

for num in range(1,51):
    if num % 3 == 0:
        my_list.append(num)
    
print(f'\nlist of nums from 1 to 50 that are divisible by 3: \n{my_list}')

#if length of word is even print even!

st = 'Print only the words that start with s in this sentence'

st_splited = st.split()
print('\n') #just to clearify

for word in st_splited:
    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)

#use list comprehension to create a list of the first letters of every word

st = 'Create a list of the first letters of every word in this string'
my_list_with_letters = []

st_splited = st.split()

for word in st_splited:
    my_list_with_letters.append(word[0])

print(my_list_with_letters)

#write a program that prints the integers from 0 to 100.
#but for multiples of 3 print 'Fizz' instead of num, and for multiples by 5 prind 'Buzz'
#for numbers which are multiples of both 3 and 5 print 'FizzBuzz'

for num in range(0, 101):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else:
        print(num)