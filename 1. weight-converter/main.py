#unfortunately python doesnt have multi-line comments :c
#weight converter from KG to LBS and back

tutorial = """
================｢HOW TO USE?｣================

『simply type in ur weight first, then system to convert』
『K - for kilograms』
『L - for pounds』

github: ｢https://github.com/doulikedarkness｣

================｢HOW TO USE?｣================
"""

print(tutorial)

weight_from_user = float(input("Tell us ur weight (no worries no data will be saved): "))

calculate_system = input("What do u want us to convert it into? (L)bs or (K)gs: ")

if calculate_system.upper() == "L":
    converted_weight = weight_from_user * 2.205
    print(f"{weight_from_user} kilograms its around~ {converted_weight} pounds")
elif calculate_system.upper() == "K":
    converted_weight = weight_from_user / 2.205
    print(f"{weight_from_user} pounds its around~ {converted_weight} kilograms")
else:
    print(f"\nDude what did u just typed in? \nHow do we turn {weight_from_user} into ur '{calculate_system}'?")
    print("[RU] Все что от тебя требуется это написать вес а потом букву, по какой системе ты хочешь конвертировать. \nK - в килограмы, L - в фунты")
    print(tutorial)
    
#endregion (yea ikr its not C#)