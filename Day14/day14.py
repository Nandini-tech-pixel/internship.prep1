def show_args(*args, **kwargs):
 print(args)
 print(kwargs)
show_args(1, 2, 3, a=10, b=20)

#ANS1
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(1,2))    
print(multiply_all(2,5,9))       
print(multiply_all(76,98))

def shout(text):
 return text.upper()
def greet(func):
 print(func("hello"))
greet(shout)

#ANS2
def apply_function(func, value):
    return func(value)
def cube(x):
    return x**3
print(apply_function(cube, 2))

def log(func):
 def wrapper():
  print("Calling function")
 func()
 return wrapper
@log
def greet():
 print("Hello")
greet()

#ANS3
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Took {end - start:.2f} seconds")
    return wrapper
@timer
def my_function():
    time.sleep(4)
    print("Done")
my_function()

from mymath import square
print(square(4))

from functions import greet, square   
print(greet("Nandini"))           
print(square(4))  

#MINI PROJECT 
def log_calls(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"Called {func.__name__} with args={args}, kwargs={kwargs}\n")
        return func(*args, **kwargs)
    return wrapper
@log_calls
def add(a, b):
    return a + b
@log_calls
def greet(name="Nandini"):
    print(f"Hello, {name}!")
print(add(2, 3))
greet()
greet(name="Saanvi")
