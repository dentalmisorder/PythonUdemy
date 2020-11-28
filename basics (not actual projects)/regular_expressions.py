import re

pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
pattern2 = r"\d{3}-\d{3}-\d{4}"
text_to_search = "You can call where you want, my phone is: 098-324-0794\nBut ask my boyfriend first, his phone is: 063-654-8743"

#first_match = re.search(pattern, text_to_search)
all_matches = re.finditer(pattern, text_to_search)


for matched_item in re.finditer(pattern2, text_to_search):
    first_id, last_id = matched_item.span()
    print(f'Found pattern: "{pattern2}" starts at index "{first_id}" end at "{last_id}", whole text found: "{matched_item.string[first_id:last_id]}"')
    
for matched_item in re.finditer(pattern, text_to_search):
    print(matched_item.group())         #bruh i could use matched_item.group() for getting the text itself...
