import re

pattern = r"(\d{3})-\d{3}-d{4}"
text_to_search = "You can call where you want, my phone is: (098)-891-0794\nBut ask my boyfriend first, his phone is: (063)-447-8743"

#first_match = re.search(pattern, text_to_search)
all_matches = re.finditer(pattern, text_to_search)

if all_matches != None:
    print('Matched something..')
    for matched_item in re.finditer(pattern, text_to_search):
        print(matched_item.span())