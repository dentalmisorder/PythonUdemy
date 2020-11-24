from collections import Counter

#its actually almost like sets
y = {2,2,2,2,2,2,'a','a','a','gawr','gawr'}

x = [2, 2, 2, 2,'a', 'a', 'a', 'a', 'gawrgura', 'gawrgura']
#i can also check words in a sentance:
sentance = 'Hewwo guys gawr gura is a best waifu shark shark shark gura'

print(Counter(sentance.split()))
print(Counter(x))
print(y)