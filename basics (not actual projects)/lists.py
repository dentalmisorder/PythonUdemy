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
