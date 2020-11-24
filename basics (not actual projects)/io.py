import os
import shutil

print(os.getcwd())

uwu = open('basics (not actual projects)\\uwu.txt', 'a+') #creating new txt file here (but move it later in OOP)
uwu.write('im wearing my programming socks rn uwu\n')

uwu.seek(0,0) #start point at start position
print(uwu.read())

uwu.close() #closing file at the end


#we can also move file
#shutil.move(current_file in path, destination path)
shutil.move('basics (not actual projects)\\uwu.txt', 'basics (not actual projects)\\oop')