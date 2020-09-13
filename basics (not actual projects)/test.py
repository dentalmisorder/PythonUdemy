s = 'hewwo'

#output should be 'o' with 2 methods using indexing

print(s[-1]) #method 1
print(s[4]) #method 2

#return 'e' from s

print(s[1])

#build list with [0,0,0] in 2 ways

list1 = [0,0,0]
[0]*3

#reasign 'hewwo' into 'goodbywe'

nested_list = [1,2,[3,4,'hewwo']]

nested_list[2][2] = 'goodbywe'

print(nested_list[2][2])

#sort the list below

unsorted_list = [1,5,6,55,12,125,7,345,22]
unsorted_list.sort()

print(unsorted_list)

#grab 'hewwo'

d = {
    'key':'hewwo'
}

d2 = {
    'key':{
        'key2':'hewwo'
    }
}

d3 = {
    'k1':[{
        'nest_key':['this is deep', ['hewwo']]
    }]
}

d4 = {
    'k1':[1,2,{
        'k2':['this is tricky' ,{
            'tough':[1,2,['hewwo']]
        }]
    }]
}

print(d['key'])
print(d2['key']['key2'])
print(d3['k1'][0]['nest_key'][1])
print(d4['k1'][2]['k2'][1]['tough'][2])

#how do u create a tuple and whats unique

#answer is tuple are immutable and cant be changed
tuple_example = ('over', 'here', 'i cant change', 'anything')

#sets and whats unique about them

#answer is they are having only one unique param
set_example = {0,0,0,0,0,1,1,1,1,2,2,2,2,3}

print(set_example)