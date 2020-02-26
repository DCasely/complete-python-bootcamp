# print('hello world')
# print('new')

# # commented out

# print('Hello World')

# # STRING INDEXING EXERCISE
# 'Hello World'[-3]

# # STING SLICING EXERCISE
# 'tinker'[1:-2]

# print('This is a string {}'.format('INSERTED'))

# print('The {} {} {}'.format('fox', 'brown', 'quick'))
# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))

# # print('---------------')
# print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))


# result = 104.1235
# print('The result was {r:1.5f}'.format(r=result))


# name = 'Jose'
# print('Hello, his name is {}'.format(name))
# print(f'Hello, his name is {name}')


# name = 'Sam'
# age = 3

# print(f'{name} is {age} years old')

# '{p} rules!'.format(p='Python')

# my_list = [1, 2, 3]

# my_list = ['STRING', 100, 23.2]
# len(my_list)

# mylist = ['one', 'two', 'three']
# mylist[0]
# mylist[1:]

# another_list = ['four', 'five']
# mylist + another_list

# mylist
# another_list

# new_list = mylist + another_list
# new_list

# new_list[0] = 'ONE ALL CAPS'
# new_list

# new_list.append('six')
# new_list

# new_list.append('seven')
# new_list

# new_list.pop()
# new_list

# popped_item = new_list.pop()
# popped_item
# new_list

# new_list.pop(0)
# new_list

# new_list = ['a', 'e', 'x', 'b', 'c']
# num_list = [4, 1, 8, 3]
# new_list.sort()
# new_list

# my_sorted_list = new_list.sort()
# type(my_sorted_list)

# # None means 'NO VALUE'

# new_list.sort()
# my_sorted_list = new_list
# my_sorted_list

# num_list
# num_list.sort()
# num_list
# num_list.reverse()
# num_list


# my_list = ['string', 24, 8.24]


# my_dict = {'key1': 'value1', 'key2': 'value2'}
# my_dict
# my_dict['key1']

# prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

# prices_lookup['apple']
# prices_lookup['oranges']
# prices_lookup['milk']

# d = {'k1':123, 'k2':[0,1,2], 'k3': {'insideKey': 100}}
# d['k2'][2]
# d['k3']
# d['k3']['insideKey']

# d = {'key1':['a','b','c']}
# mylist = d['key1']
# mylist
# letter = mylist[2]
# letter
# letter.upper()

# d['key1'][1].upper()

# d = {'k1':100, 'k2':200}
# d['k3'] = 300
# d

# d.values()

# d.keys()

# d.items()

# {'key1': 1, 'key2': 2}


# t = (1, 2, 3)
# mylist = [1, 2, 3]

# type(t)
# type(mylist)

# len(t)
# len(mylist)

# t = ('one', 2)
# t[0]

# t[-1]

# t = ('a', 'a', 'b')
# t.count('a')

# t.index('a')
# t.index('b')

# mylist[0] = 'NEW'
# mylist

# ========================================

# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(2)  # ONLY UNIQUE VALUES

# mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
# set(mylist)

# city = 'Mississippi'
# set(city)

# True
# False
# type(False)
# type(True)

# 1 > 2
# 1 == 1

# b = None

# set([1, 1, 2, 3])

# myfile = open('adsfadfmyfile.txt')  # Wrong file alert
# myfile = open('myfile.txt')
# myfile.read()

# myfile.read()  # need to reset cursor to read again

# myfile.seek(0)
# myfile.read()

# content = myfile.read()
# content

# myfile.seek(0)
# myfile.readlines()

# myfile.close()

# with open('myfile.txt') as my_new_file:
#     contents = my_new_file.read()
# contents

# with open('myfile.txt', mode='a') as myfile:
#     contents = myfile.read()

# contents


# with open('my_new_file.txt', mode='r') as f:
#     print(f.read())


# with open('my_new_file.txt', mode='a') as f:
#     f.write('FOUR ON FOURTH')

# with open('my_new_file.txt', mode='r') as f:
#     print(f.read())

# with open('adadfkajhasdfkh.txt', mode='w') as f:
#     f.write('I CREATED THIS FILE!')

# with open('adadfkajhasdfkh.txt', mode='r') as f:
#     print(f.read())

# with open('test.txt', mode='w') as x:
#     x.write('Hello World')
#     x.close()
