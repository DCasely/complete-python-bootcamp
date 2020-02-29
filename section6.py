# =====================================
# METHODS AND THE PYTHON DOCUMENTATION
# =====================================

# mylist = [1,2,3]

# mylist.append(4)

# mylist.pop()

# mylist.insert


# =====================================
# FUNCTIONS IN PYTHON
# =====================================

# def name_function():
#     '''
#     DOCSTRING: Information about the function
#     INPUT: no input...
#     OUTPUT: Hello...
#     '''
#     print('Hello')

# name_function()

# def say_hello(name):
#     print('hello ' +name)

# say_hello('Davin')

# def say_hello(name='NAME'):
#     return 'hello ' +name

# say_hello('David')

# result = say_hello('Zach')

# result

# def add(n1, n2):
#     return n1 + n2


# result = add(20, 30)

# Find out if the word 'dog' is in a string?

# def dog_check(mystring):
#     return 'dog' in mystring.lower()

# dog_check('Dog ran away')

# def pig_latin(word):

#     first_letter = word[0]

#     # check if vowel
#     if first_letter in 'aeiou':
#         pig_word = word + 'ay'
#     else:
#         pig_word = word[1:] + first_letter + 'ay'

#     return pig_word

# word = pig_latin('apple')


# ========================================================
#  CODING EXERCISE 10: FUNCTIONS #1: print HELLO WORLD
# ========================================================


# def myfunc(name):
#     print('Hello World')

# ========================================================
#  CODING EXERCISE 11: FUNCTIONS #2: print Hello Name
# ========================================================


# def myfunc(name):
#     print(f'Hello {name}')

# ========================================================
#  CODING EXERCISE 12: FUNCTIONS #3: simple Boolean
# ========================================================


# def myfunc(x):
#     if x:
#         return 'Hello'
#     else:
#         return 'Goodbye'

# ========================================================
#  CODING EXERCISE 13: FUNCTIONS #4: using Boolean
# ========================================================


# def myfunc(x, y, z):
#     if z:
#         return x
#     else:
#         return y

# ========================================================
#  CODING EXERCISE 14: FUNCTIONS #5: simple math
# ========================================================


# def myfunc(x, y):
#     return x + y

# ========================================================
#  CODING EXERCISE 15: FUNCTIONS #6: is even
# ========================================================


# def is_even(num):
#     return num % 2 == 0

# ========================================================
#  CODING EXERCISE 16: FUNCTIONS #7: is greater
# ========================================================


# def is_greater(x, y):
#     return x > y or y <= x

# ========================================================
#  CODING EXERCISE 17: FUNCTIONS #8: *args
# ========================================================


# ========================================================
#  CODING EXERCISE 18: FUNCTIONS #9: pick evens
# ========================================================


# ========================================================
#  CODING EXERCISE 19: FUNCTIONS #10: skyline
# ========================================================

# def myfunc(a, b):
#     # Returns 5% of the sum of a and b
#     return sum((a, b)) * 0.05


# result = myfunc(40, 60)

# def myfunc(*args):
#     return sum(args) * 0.05


# result = myfunc(40, 60, 100, 1, 34)


# def myfunc(*args):
#     for item in args:
#         print(item)

# myfunc(40,60,100,1,34)

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')


# myfunc(fruit='apple', veggie='lettuce')


# def myfunc(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print('I would like {} {}'.format(args[0], kwargs['food']))


# myfunc(10, 20, 30, 'apple', fruit='orange', food='eggs', animal='dogs')


# ========================================================
#  FUNCTION #8: *ARGS
# ========================================================

# def myfunc(*args):
#     return sum(args)

# ========================================================
#  FUNCTION #9: PICK EVENS
# ========================================================

# def myfunc(*args):
#     return list(num for num in args if num%2 == 0)

# result = myfunc(1,2,3,4,5,6,7)

# ========================================================
#  FUNCTION #10: SKYLINE
# ========================================================

# def myfunc(word):
#     new_string = ''
#     for index, letter in enumerate(word):
#         if index%2 == 0:
#             new_string += letter.upper()
#         else:
#             new_string += letter.lower()

#     return new_string

# result = myfunc('haldaserkjealea')

# ========================================================
#  FUNCTION PRACTICE EXERCISES
# ========================================================


# def master_yoda(text):
#     seperated = text.split()
#     reversed = seperated.reverse()
#     return reversed.join()

# x = 'I love you'

# result = ' '.join(reversed(x.split()))

# mylist = [1,2,3,4]
# myjoin = ''.join(str(n) for n in mylist)

# def has_33(nums):
#     return  '33' in ''.join(str(x) for x in nums)

# result = has_33([1, 3, 1, 3,3])


# def paper_doll(text):
#     triple = ''
#     for letter in text:
#         triple += letter*3
#     return triple


# result = paper_doll('Mississippi')


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5, 6, 7) - -> 18
# blackjack(9, 9, 9) - -> 'BUST'
# blackjack(9, 9, 11) - -> 19

# def blackjack(a, b, c):
#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) > 21:
#         if a == 11 or b == 11 or c == 11:
#             return sum((a, b, c)) - 10
#         else:
#             return 'BUST'


# result = blackjack(9, 9, 8)

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) - -> 9
# summer_69([4, 5, 6, 7, 8, 9]) - -> 9
# summer_69([2, 1, 6, 9, 11]) - -> 14


# def summer_69(arr):
#     mysum = 0
#     for x in arr:
#         if x < 6 or x >9:
#             mysum += x

#     return mysum


# result = summer_69([4, 5, 6, 7, 8, 9])

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1, 2, 4, 0, 0, 7, 5]) - -> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) - -> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) - -> False


# def has_33(nums):
#     return  '33' in ''.join(str(x) for x in nums)

# result = has_33([1, 3, 1, 3,3])

# def spy_game(nums):
#     return '007' in ''.join(str(x) for x in nums)


# result = spy_game([1, 2, 4, 0, 0, 7, 5])

# result = list(range(0, 101))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) - -> 25
# By convention, 0 and 1 are not prime.

# def count_primes(num):
#     myrange = list(range(0, num))
#     prime_count = 0
#     for x in range(0, num):
#         prime_count += 1


# def count_primes(num):
#     primelist = [x for x in range(2, num+1) if not [
#         t for t in range(2, x) if not x % t]]

#     return len(primelist)


# # result = count_primes(100)

# def count_primes(num):
#     # Check for 0 or 1 input
#     if num < 2:
#         return 0
#     ###################
#     # 2 of greater
#     ###################

#     # Store our prime numbers
#     primes = [2]
#     # Counter going up to the input num
#     x = 3

#     # x is going through every number up to the input num
#     while x <= num:
#         for y in primes:
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)


# result = count_primes(100)


# ========================================================
#  LAMBDA EXPRESSIONS, MAP, AND FILTER FUNCTIONS
# ========================================================

# def square(num):
#     return num**2


# my_nums = [1, 2, 3, 4, 5]

# for item in map(square, my_nums):
#     print(item)

# result = list(map(square, my_nums))


# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]


# result2 = list(map(splicer, names))


# def check_even (num):
#     return num%2 == 0

# mynums = [1,2,3,4,5,6]

# # result = list(filter(check_even,mynums))

# lambda num: num ** 2
# square(3)

# list(map(lambda num:num**2, mynums))

# result =list(filter(lambda num: num%2 == 0, mynums))

# names = ['Andy', 'Eve', 'Sally']

# list(map(lambda x: x[0], names))
# list(map(lambda x: x[::-1], names))


# ========================================================
#  NESTED STATEMENTS AND SCOPE
# ========================================================

# x = 25

# def printer()
#     x = 50
#     return x

# print(x)

# lambda num: num**2

# GLOBAL
# name = 'THIS IS A GLOBAL STRING'

# def greet():

#     # ENCLOSING
#     # name = 'Sammy'

#     def hello():
#         # LOCAL
#         # name = 'IM A LOCAL'
#         print('Hello ' + name)

#     hello()


# greet()


# x = 50


# def func(x):

#     print(f'X is {x}')

#     # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
#     x = 'NEW VALUE'
#     print(f'I JUST LOCALLY CHANGED X TO {x}')
#     return x

# x = func(x)

# print(x)

# ========================================================
#  FUNCTIONS AND METHODS - HOMEWORK ASSIGNMENT
# ========================================================

# import math

# def vol(rad):
#     # 4/3π * radius
#     return 4/3*math.pi*rad**3

# result = vol(2)

# def ran_check(num, low, high):
#     if num >= low or num <= high:
#         return f'{num} is in the range between {low} and {high}'


# result = ran_check(5, 2, 7)


# def ran_bool(num, low, high):
#     return num >= low or num <= high


# result = ran_bool(3, 1, 10)


# def up_low(s):
#     uppercase = 0
#     lowercase = 0

#     for letter in s:
#         if letter.isupper():
#             uppercase += 1
#         elif letter.islower():
#             lowercase += 1

#     return f'Uppercase Count: {uppercase}\nLowercase Count: {lowercase}'


# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# result = up_low(s)

# print(result)

# def unique_list(lst):
#     return list(set(lst))


# # result = unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])

# def multiply(numbers):
#     result = 1

#     for x in numbers:
#         result *= x

#     return result

# # import functools import reduce

# # def multiply2(numbers):
# #     return reduce(lambda x, y: x*y, numbers)

# result = multiply([1,2,3,-4])
# # result2 = multiply2([1,2,3,-4])


# def palindrome(s):
#     return s == s[::-1]


# result = palindrome('helleh')


import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    abccount = []

    for letter in str1.lower():
        if letter not in abccount and letter != ' ':
            abccount.append(letter)

    return len(abccount) == 26


result = ispangram("The quick brown fox jumps over the lazy dog")
