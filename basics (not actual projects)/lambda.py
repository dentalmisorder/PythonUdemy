num_list = [1,2,3,4,5,6]

def square(num):
    return num**2

map_list = list(map(square, num_list))
print(map_list)

#expressions
num_list = [1,2,3,4,5,6]

map_list = list(map(lambda num: num**2, num_list))
print(map_list)