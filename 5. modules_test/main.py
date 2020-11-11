import hints
from users_lib import player
from users_lib import admin

Spylestia = player.Player('Spylestia', 1, 'farmer',12,555)
Admin = admin.Admin('DoULikeDarkness', 999, 'Creator', 999, 999)

hints.show_all_players()
hints.about_stats()