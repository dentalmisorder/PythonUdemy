#dictionary

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Tsero"
}

input_user = input("Insert numbers with space: ")

nums = input_user.split()

for num in nums:
    print(numbers[num])

#=======================================

prices = {
    "apple":2.99,
    "orange":5.99,
    "banana":3.99,
    "ores":{
        "iron":9.99,
        "coal":6.99,
        "gold":18.99,
        "platinum":16.50
    }
}

print(f'\nprice of an apple is {prices["apple"]}') #simple use with key-value pair
print(f'\nprice of an ore -> coal is: {prices["ores"]["coal"]}') #coal cost in dictionary inside of another dictionary

prices["ores"]["diamond"] = 99.99 #adding one more ore

print(f'\nprice of all ores: {prices["ores"]}') #list of all ores

#======================more practice===============

currency = "₽ (ruble)"
my_games_prices = {
    "Animal Crossing 2" : 399.99,
    "Jump to rescue cuties" : 99.99,
    "NSFW" : {
        "Schoolgirls summer work" : 299.99,
        "Anime tiddie island" : 299.99
    }
}

print(f"\nJump to rescue cuties costs: {my_games_prices['Jump to rescue cuties']}{currency}")
print(f"\nAnime tiddie island costs: {my_games_prices['NSFW']['Anime tiddie island']}{currency}")
print(f"all the titles names i published: {my_games_prices.keys()}")