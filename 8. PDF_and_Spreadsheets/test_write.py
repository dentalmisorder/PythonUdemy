import csv

file = open('8. PDF_and_Spreadsheets\\new_file.csv',mode='w+',newline='')

writer = csv.writer(file,delimiter=';')

writer.writerow(['1', 'Freyja', 'Grandmaster', 'https://www.artstation.com/doulikedarkness'])
writer.writerow(['2', 'doulikedarkness', 'Master', 'https://vk.com/doulikedarkness'])
writer.writerow(['3', 'Spylestia', 'Diamond', 'https://discord.gg/NPKTF3Nbad'])
