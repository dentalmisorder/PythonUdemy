import re
import os

phone_pattern = r'\d{3}-\d{3}-\d{4}'

phones = open('phones.txt', 'w+')

for folder, subfolders, files in os.walk('extracted_content'):
    print(f'Folder: {folder}:')
    
    for subfolder in subfolders:
        print(f'Subfolder: {subfolder}')
        for file in files:
            print(f'File: {file}')
            opened_file = open(f'{folder}\\{subfolder}\\{file}', 'a+')
            opened_file.seek(0,0)
            x = re.search(phone_pattern, opened_file.read())
            if type(x) is not type(None):
                for item in x:
                    phones.write(item)
            opened_file.close()

    for file in files:
        print(f'File: {file}')
        opened_file = open(f'{folder}\\{file}', 'a+')
        opened_file.seek(0,0)
        x = re.findall(phone_pattern, opened_file.read())
        if type(x) is not type(None):
            for item in x:
                phones.write(item)
        opened_file.close()

            
phones.close()