#sets is basically lists with unique items, so they dont repeat

#look at that:
my_set = {1,2,2,2,2,2,3,3,3,3,4} #result is {1, 2, 3, 4}

print(my_set)

#we also can convert lists into a set

my_list = [1,2,2,2,1,1,2,1,2] #result is [1, 2, 2, 2, 1, 1, 2, 1, 2]
print(set(my_list)) #but now result is {1, 2}