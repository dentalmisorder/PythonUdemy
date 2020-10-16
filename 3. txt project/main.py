myfile = open('juice wrld - lucid dreams.txt')
list_of_files = {
    '1':'iann dior - cutthroat', 
    '2':'juice wrld - lucid dreams'
}

input_file = input(f"\n{list_of_files}\nWhich of files you wanna see (type in number)?: ")
file_to_open = list_of_files[input_file]
print(f'\nYouve chosen {file_to_open}')

while True:
    if input_file == '1':
        myfile = open('iann dior - cutthroat.txt')
        break
    elif input_file == '2':
        myfile = open('juice wrld - lucid dreams.txt')
        break
    else:
        print("Whoops, u did not typed in a number of file u wanted, try again")
    

print(myfile.read())