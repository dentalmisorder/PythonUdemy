prices = [3.55, 2.99, 3.99, 6.99, 9.99]

total_price = 0.0
for price in prices:
    total_price += price
    print(f"Adding item that costs {price}$")

print(f"Total: {total_price}")

#more practice

for letter in 'hewwo':
    print(letter) #u can print every letter in string cause its also a list of letters

my_published_games = {
    'Anime tiddie goths': 2.99,
    'Witch nekos': 5.99,
    'Farm and grow': 9.99
}

for game_name, game_price in my_published_games.items():
    print(f'Game title: {game_name} | Price: {game_price}$')