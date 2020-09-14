#============found the largest number============

massive_of_nums = [5,7,12,4,3,157,234,1333,7563,234,554,2346,6000,7235]
largest_item = massive_of_nums[0]

for item in massive_of_nums:
    if item > largest_item:
        largest_item = item
print(f"Largest int was {largest_item}")

#============remove duplicates from list============

nums = [234,324,323,52,352,52,42,342,423,42,423,42]

nums.sort() #sorting just for visual clearence

print(nums) #nums with duplicates

for num in nums:
    if nums.count(num) > 1:
        nums.remove(num)

print(nums) #nums without duplicates

#============remove duplicates from list alternative ============

nums = [2,2,3,3,4,6,3,4,7,2,1]
nums_unique = []  #new unique list (empty)

nums.sort() #sorting just for visual clearence

print(nums) #nums with duplicates

for num in nums:
    if num not in nums_unique: #looking if new list has that num
        nums_unique.append(num) #if not adding it to new list

print(nums_unique) #nums without duplicates

#===============remove last===================

phrase = "all i want from life is small tiddie goth anime bich"

phrase = phrase.split()

print(phrase)

phrase.pop() #will remove last by default or u can insert index (changes are saving tho)

print(phrase)

phrase.append("gf") #same but with adding in the end

print(phrase)

#=========== zipping

my_list1 = [0,1,2,3,4,5]
my_list2 = ['a','b','c']

for a,b in zip(my_list1, my_list2):
    print(a,b) #we can do unpacking like this with 2 variables

for item in zip(my_list1, my_list2):
    print(item) #or we can do the same like that

#==============
my_list = []

for word in 'hewwo':
    my_list.append(word)

print(my_list)