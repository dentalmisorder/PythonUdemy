def ten_percent(*args): #args just using it as a tuple
    print(args)
    return sum(args) * 0.1  #just to clarify u still can do operations on that tuple

def test_dictionaries(**kwargs): #kwargs instead using it as a dictionary
    print(kwargs)

print(f'10 percent out of this sum is {ten_percent(20,20,10,10,10,20,10)}') #now u can give any amount of numbers
test_dictionaries(emotions = ['angry', 'rather be dead', 'depressed', 'cant take the pain', 'feeling hopeless'])
