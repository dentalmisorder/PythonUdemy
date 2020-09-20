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

singers_songs = [('iann dior', 8), ('juice wrld', 12), ('guccihighwaters', 6), ('familypet', 21), ('93feetofsmoke', 16)]

#decalring functions

def most_songs(singers_and_songs_count): #tuple unpacking with funcs
    max_songs = 0
    max_singer = ''

    for singer, songs_count in singers_and_songs_count:
        if(songs_count > max_songs):
            max_songs = songs_count
            max_singer = singer
        else:
            pass
    print(f'{max_singer} got the most songs out of all with count of {max_songs}')

def my_anime_list():
    for num, title_name in anime_list.items(): #unpacking
        print(title_name)

def my_opening_list():
    for anime_name, op_name in opening_list.items(): #unpacking to use separately key and value
        print(f'Favorite tracks from "{anime_name}":\n{op_name}\n')

#executing

my_anime_list() #calling the func
my_opening_list() #calling the func
most_songs(singers_songs) #calling the func and giving it a value to work with