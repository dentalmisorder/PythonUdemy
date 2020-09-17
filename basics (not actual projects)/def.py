#decalring dictionaries

anime_list = {
    1:'Re:Creators',
    2:'Kimi No Na Wa',
    3:'Black Clover',
    4:'Paprika',
    5:'Evangelion Neon Genesis',
    6:'Perfect Blue'
}

opening_list = {
    'Black Clover':['TOMORROW X TOGETHER — Everlasting Shine (12 OP)', 'Vickeblanka — Black Catcher (10 OP)', 'Vickeblanka — Black Rover (3 OP)', 'Seiko Oomori — JUSTadICE (7 OP)','Kankaku Piero - Haruka Mirai (1 OP)'],
    'RE:Creators':['Sawano Hiroyuki [nZk]: Tielle and Eliana — AL:Lu', 'Eliana — BRAVE THE OCEAN', 'SawanoHiroyuki — sh0ut (2 OP)', 'Aimee Blackschleger — Layers', 'SawanoHiroyuki[nZk] — gravityWall (1 OP)'],
    'Kimi no na wa':['RADWIMPS — Sparkle', 'RADWIMPS — Yumetourou', 'RADWIMPS — Nandemonaiya']
}

#decalring functions

def my_anime_list():
    for num, title_name in anime_list.items(): #unpacking
        print(title_name)

def my_opening_list():
    for anime_name, op_name in opening_list.items(): #unpacking to use separately key and value
        print(f'Favorite tracks from "{anime_name}":\n{op_name}\n')

#executing

my_anime_list() #calling the func
my_opening_list() #calling the func