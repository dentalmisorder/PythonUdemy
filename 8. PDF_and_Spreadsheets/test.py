import csv

file_to_read = open('8. PDF_and_Spreadsheets\\example.csv',encoding='utf-8')

#file_to_read.seek(0)

csv_file = list(csv.reader(file_to_read))
how_many_results = 100

print(f'''
First {how_many_results} results:
=================================================================================
{csv_file[0]}
=================================================================================
''')

for line in csv_file[1:how_many_results]:
    if 'female' in line[4].lower():
        print(f'[ID: {line[0]}] | Name: {line[1]} {line[2]} | Gender: {line[4]} | Address: {line[6]}')

file_to_read.close()