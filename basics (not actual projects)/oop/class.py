class Player():
    players_list = []
    pvp_mode = True
    last_player_registered = 0

    def __init__(self, player_name, player_lvl, player_job, player_adaptability, player_creativity):
        self.name = player_name
        self.lvl = player_lvl
        self.job = player_job
        self.adaptability = player_adaptability
        self.creativity = player_creativity
        Player.last_player_registered+=1
        self.id = Player.last_player_registered

        print("\n✿ New player just registered! ✿\nHewwo {} he is {} player registered!\n".format(self.name, self.id))

        Player.players_list.append(self)
    
    def show_stats(self):
        print("""
        ========={0}'s STATS========
        Level: {1}★
        Job: {2}
        Adaptability: {3}⎔
        Creativity: {4}✾
        ================================
        """.format(self.name, self.lvl, self.job, self.adaptability, self.creativity))

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

    def show_all_players(self):
        print("\n======[ALL PLAYERS REGISTERED]======")
        print("""
YOUR ID: {0} | YOUR NAME: {1} | YOUR JOB: {2} | YOUR LVL: {3} | YOUR PVP MODE: {4}
        """.format(self.id, self.name, self.job, self.lvl, self.pvp_mode))
        for plr in Player.players_list:
            print(f"ID: {plr.id} | Name: {plr.name} | PVP Mode: {Player.pvp_mode}")
        print("====================================\n")

class Admin(Player):
    def ban_player(self, player_to_ban):
        Player.players_list.remove(player_to_ban)
        print("""
        ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖
        ✂ Player {0} got banned by {1}
        ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖
        """.format(player_to_ban.name, self.name))

#all players have names, lvl, their job (class), stamina, and crafting lvl to explore new things
MARSvechen = Player("MARS", 3, "Farmer", 12, 87)
Spylestia = Player("Spylestia", 3, "Alchemist", 6, 91)
BrandNewPlayer = Player("BrandNewPlayer", 55, "Artist", 3, 287)
Toxic228 = Player("Toxic228", 1, "Garbage Collector", 2, 5)

#creating ADMIN but still a PLAYER inherited class
doulikedarkness = Admin("DoULikeDarkness", 9999, "Creator", 9999, 9999)

Spylestia.show_all_players() #all players list (they all have pvp mode)

print("For today we are celebrating Halloween! And turning off PvP mode!")
Player.pvp_mode = False

MARSvechen.show_all_players() #all players list (as u can see all no pvp mode)

doulikedarkness.ban_player(Toxic228) #banning a player that are toxic

Spylestia.show_all_players() #showing list again (no toxic players found xd)
