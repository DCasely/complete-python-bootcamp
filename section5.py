# =====================================
# IF ELIF AND ELSE STATEMENTS IN PYTHON
# =====================================

# hungry = True

# if hungry:
#     print('FEED ME!')
# else:
#     print('Im not hungry')

# loc = 'Bank'

# if loc == 'Auto Shop':
#     print('Cars are cool!')
# elif loc == 'Bank':
#     print('Money is cool!')
# elif loc == 'Store':
#     print('Welcome to the store!')
# else:
#     print('I do not know much.')

# name = 'Sammy'

# if name == 'Frankie':
#     print('Hello Frankie!')
# elif name == 'Sammy':
#     print('Hello Sammy')
# else:
#     print('What is your name?')


# =====================================
# FOR LOOPS IN PYTHON
# =====================================

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in mylist:
#     print('hello')

# for num in mylist:
#     # Check for even
#     if num % 2 == 0:
#         print(f'Even Number: {num}')
#     else:
#         print(f'Odd Number: {num}')


# list_sum = 0

# for num in mylist:
#     list_sum += num

# print(list_sum)


# mystring = 'Hello World'
# for _ in mystring:
#     print('Cool!')


# tup = (1,2,3)

# for item in tup:
#     print(item)

# mylist = [(1,2), (3,4), (5,6), (7,8)]

# len(mylist)

# for a, b in mylist:
#     print(b)


# mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# for item in mylist:
#     print(item)

# for a, b, c in mylist:
#     print(c)


# d = {'k1': 1, 'k2': 2, 'k3': 3}

# for key in d:
#     print(key)

# for key, value in d.items():
#     print(value)

# for value in d.values():
#     print(value)

# =====================================
# WHILE LOOPS IN PYTHON
# =====================================

# x = 50

# while x < 5:
#     print(f'The current value of x is {x}')
#     x += 1
# else:
#     print('X IS NOT LESS THAN 5')


# x = [1,2,3]

# for item in x:
#     # comment
#     pass
# print('end of my script')

# mystring = 'Sammy'

# for letter in mystring:
#     if letter == 'a':
#         continue
#     print(letter)


# for letter in mystring:
#     if letter == 'm':
#         break
#     print(letter)

# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1


# =====================================
# USEFUL OPERATORS IN PYTHON
# =====================================

# for num in range(3, 10, 3):
#     print(num)

# print(list(range(0, 11, 2)))


# for letter in 'abcde':
#     print(f'At index {index_count} the letter is {letter}')
#     index_count += 1

# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(word[index_count])
#     index_count += 1


# word = 'abcde'

# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')

# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
# mylist3 = [100, 200, 300]
# for item in zip(mylist1, mylist2, mylist3):
#     print(item)

# list(zip(mylist1, mylist2))

# 'x' in [1, 2, 3]

# 2 in [1, 2, 3]

# 'x' in ['x', 'y', 'z']

# 'a' in 'a world'

# 'mykey' in {'mykey': 345}

# d = {'mykey': 345}
# 345 in d.values()
# 345 in d.keys()


# mylist = [10,20,30,40,100]

# min(mylist)

# max(mylist)

# from random import shuffle

# mylist = [1,2,3,4,5,6,7,8,9,10]

# shuffle(mylist)

# random_list = shuffle(mylist)

# print(random_list) #None
# print(mylist)

# from random import randint

# x = randint(0,100)
# y = randint(0,100)

# result = input('Enter a number here: ')
# result = input('What is your name? ')
# result = input('Favorite Number: ')

# =====================================
# LIST COMPREHENSIONS IN PYTHON
# =====================================

# mystring = 'hello'

# mylist = []

# for letter in mystring:
#     mylist.append(letter)

# mystring = 'hello'

# mylist = [letter for letter in mystring]

# mylist = [x for x in 'wordtwo']

# mylist = [num**2 for num in range(0,11)]

# mylist = [x**2 for x in range(0,11) if x%2 == 0]

# celcius = [0,10,20,34.5]

# fahrenheit = [((9/5)*temp + 32) for temp in celcius]

# celcius = [0, 10, 20, 34.5]
# fahrenheit = []

# for temp in celcius:
#     fahrenheit.append(((9/5)*temp + 32))

# results = [x if x%2==0 else 'ODD' for x in range(0,11)]

# mylist = []

# for x in [2,4,6]:
#     for y in [1,10,1000]:
#         mylist.append(x*y)


# mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
