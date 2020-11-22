import colorama
colorama.init(autoreset=True)

my_fav_songs_list = {
    'iann dior':['emotions', 'romance361', '18', 'molly', 'crash my whip', 'cutthroat', 'gone girl'],
    'BABYMETAL':['Shanti Shanti Shanti', 'Road of Resistance', 'PA PA YA', 'AKATSUKI', 'Megitsune', 'KARATE'],
    'Allman Brown':['Moonlight', 'House of Spirits', 'Hollows', 'Your Love', 'Sons & Daughters', 'Foolish Love'],
    'The Killers':['Brightside', 'Read My Mind'],
    'alt-j':['matilda', 'something good', 'lovely day', 'bloodflood'],
    'Ed Sheeran':['Shape of You', 'Castle on the Hill', 'Bloodstream', 'Cold Coffee', 'Kiss me', 'Drunk']
}

def confirm_action(func):
    def wrap_up():
        user_input = ''

        while True:
            print(f"{colorama.Fore.RED} This action you CANNOT UNDO! Choose wisely!")
            user_input = input('Are you sure? [Yes/No]: ')
            if 'no' in user_input.lower():
                print(f'{colorama.Fore.GREEN} Wise choice! c:\nHave a wonderful day cutie!')
                return wrap_up
            elif 'yes' in user_input.lower():
                func()
                print(f"We've done what you wanted.\nHope no one sad :c")
                break
    return wrap_up

@confirm_action
def clear_playlist():
    for artist, song_name in my_fav_songs_list.items():
        print(f'{colorama.Fore.RED} {artist} | {song_name}')
    my_fav_songs_list.clear()
    print(f'\n{colorama.Fore.GREEN} Current song list: {my_fav_songs_list}')


if __name__ == "__main__":
    clear_playlist()

colorama.deinit()