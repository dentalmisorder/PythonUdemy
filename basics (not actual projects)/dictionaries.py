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

input_user = input("Phone: ")

nums = input_user.split()

for num in nums:
    print(numbers[num])