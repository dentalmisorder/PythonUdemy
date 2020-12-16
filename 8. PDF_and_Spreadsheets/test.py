import csv

file_to_read = open('8. PDF_and_Spreadsheets\\example.csv',encoding='utf-8')

#file_to_read.seek(0)

csv_file = list(csv.reader(file_to_read))

print(f'''
=================================================================================
{csv_file[0]}
=================================================================================
''')

for line in csv_file[1:5]:
    print(line)

file_to_read.close()