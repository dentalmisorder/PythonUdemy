import os
import shutil
import send2trash
import colorama

colorama.init(autoreset=True)

print(os.getcwd())

uwu = open('basics (not actual projects)\\uwu.txt', 'a+') #creating new txt file here (but move it later in OOP)
uwu.write('im wearing my programming socks rn uwu\n')

uwu.seek(0,0) #start point at start position
print(uwu.read())

uwu.close() #closing file at the end


#we can also move file
#shutil.move(current_file in path, destination path)
shutil.move('basics (not actual projects)\\uwu.txt', 'basics (not actual projects)\\oop')

send2trash.send2trash('basics (not actual projects)\\oop\\uwu.txt')
#ofc sends it to trash


#os.walk(path) walks and check every folder, then subfolder then file and returns tuple that we can unpack

print(f'{colorama.Fore.RED} We are opening {os.getcwd()}..\n')

for folder, subfolders, files in os.walk(os.getcwd()): #os.getcwd gets the current directory (returning str)
    if '.git' in folder or 'pycache' in folder: #something like .gitignore, ignoring .git shit
        continue
    print(f'\n>CURRENT FOLDER: \n{folder}\n')

    if len(subfolders) > 0:
        print('>>SUBFOLDERS INSIDE: ')
        for subfolder in subfolders:
            print(f'\t{subfolder}')
    
    print('>>>FILES INSIDE FOLDER:')
    for file in files:
        print(f'\t\t{file}')

colorama.deinit()