from users_lib import player

def about_stats(self):
    print("""
        ================================
        Level - Level gaining by exp
        collecting, you can get exp by
        doing regular things or x3 exp
        by doing your job things and x5
        exp by doing yout job FAV things
        (FAV things mentioned with ❥);

        Job - Basically a class, but not
        like warrior or mage, you can do
        anything you want but you can do
        better with things that somehow
        similiar to your job (For
        example Artist can create things
        better then everyone else cause
        they got more base CREATIVITY ✾)

        Creativity ✾ - For every move you 
        do that matches your job you get 
        exp to power up level ★ and get 
        CREATIVITY ✾ if you explore 
        something new, with this ✾ 
        points you can create and do 
        more stuff then you knew you
        could before! Explore and try new
        things, unlock your creativity

        Adaptability ⎔ - Is a paramether 
        that declares how many things or
        moves you can do per day without 
        getting bored or tired.
        ================================
    """)

def show_all_players():
    print("\n======[ALL PLAYERS REGISTERED]======")
    for plr in player.Player.players_list:
        print(f"ID: {plr.id} | Name: {plr.name} | PVP Mode: {player.Player.pvp_mode}")
    print("====================================\n")