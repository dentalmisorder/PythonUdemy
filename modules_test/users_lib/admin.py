from . import player

class Admin(player.Player):
    def ban_player(self, player_to_ban):
        player.Player.players_list.remove(player_to_ban)
        print("""
        ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖
        ✂ Player {0} got banned by {1}
        ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖ ✖
        """.format(player_to_ban.name, self.name))

if __name__ == '__main__':
    print('admin lib from users_lib loaded directly..')
else:
    print('admin from users_lib imported..')