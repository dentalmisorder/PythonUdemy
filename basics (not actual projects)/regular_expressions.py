import re

pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
pattern2 = r"\d{3}-\d{3}-\d{4}" #same as before but more clear (and better cause scalable)
pattern3 = re.compile(r"(\d{3})-(\d{3})-(\d{4})") #compile into Pattern Obj with 3 groups to call them separately
pattern4 = r"call (me|him|her|my|them|they|your)" #basically an | or operator like || in other langs
pattern5 = r"meow...."
pattern6 = r"[\w]+-[\w]+"

text_to_search = "You can call me whenever you want, my phone is: 098-324-0794\nBut call my boyfriend first, his phone is: 063-654-8743"
ama_kittycat = "Good meowning, nyanners, how was ur Meownday? :з"
text3 = "go-go guys, we are hype-in!"

first_match = re.search(pattern, text_to_search) #to find only one match use re.search(patter, text)
all_matches = re.finditer(pattern, text_to_search) #to find all matches use re.finditer(pattern, text) or findall


for matched_item in re.finditer(pattern2, text_to_search): #my own try without groups (didnt knew i could do that)
    first_id, last_id = matched_item.span()
    print(f'Found pattern: "{pattern2}" starts at index "{first_id}" end at "{last_id}", whole text found: "{matched_item.string[first_id:last_id]}"')
    
for matched_item in re.finditer(pattern, text_to_search):
    print(matched_item.group())         #bruh i could use matched_item.group() for getting the text itself...

for matched_item in re.finditer(pattern3, text_to_search):
    print(matched_item.group(1))        #index at groups start from 1 not from 0 :)

print(re.findall(pattern4, text_to_search))

print(re.findall(pattern5, ama_kittycat.lower()))

print(re.findall(pattern6, text3))
