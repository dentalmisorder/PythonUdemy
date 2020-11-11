import math

try:
    for i in [1, 2, 3]:
        print(math.sqrt(i))

    x = 0 / 0
    print(x)
except TypeError:
    print("Whooops! Looks like u tried to do some math without nums")
except ZeroDivisionError:
    print("Bruh dude what are u doing? U r trying to divide by 0!")
finally:
    print('i dont care about ur exceptions im looking fresh dude')