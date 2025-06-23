from functools import reduce

double = lambda x: x * 2
print(double(4))

#ANS1
cube = lambda x: x ** 3
print(cube(6)) 

nums = [1, 2, 3]
squares = list(map(lambda x: x**2, nums))
print(squares)

#ANS2
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

#ANS3
nums = [1, 2, 3, 4,5,6,7,8]
odds = list(filter(lambda x: x%2!=0, nums))
print(odds)

from functools import reduce
nums = [1, 2, 3, 4]
prod = reduce(lambda x, y: x*y, nums)
print(prod)

from functools import reduce
numbers = [2,11,9,7,18,23,4]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum value:", max_value)

#Mini project 
grades = [90,91,80,78,82,71,20,32,70,16,42]
passing = list(filter(lambda x: x >= 40, grades))
print("Passing grades:", passing)
