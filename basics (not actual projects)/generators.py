import random
#1.Create a generator that generates the sqr of nums up to some num NUM:

def generate_sqr(num):
    for n in range(num):
        yield n**2

print(generate_sqr(10)) #generator at x030430 memory locate
for n in generate_sqr(10): #actually calling it to print these nums
    print(n)

#2. Create a generator that generates NUM random nums beetween low and high num of input

def generate_rnd(low_num, high_num, amount):
    for item in range(amount):
        yield random.randint(low_num, high_num)

print(generate_rnd(15,22,5)) #generator at x030430 memory locate
for n in generate_rnd(15,22,5): #actually calling it to print these nums
    print(n)