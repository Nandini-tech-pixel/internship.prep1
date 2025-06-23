def greet():
 print("Hello!")

#ANS1
def print_name_age():
    name = "Nandini"
    age = 20
    print("Name:", name)
    print("Age:", age)
print_name_age()

def add(a, b):
 return a + b
result = add(3, 5)
print(result)

#ANS2
def square_number(num):
    return num ** 2
result = square_number(3)
print("Square:", result)

x = 10
def change():
 x = 5
print("Inside:", x)
change()
print("Outside:", x)

#ANS3
value = 10
def compare_with_global():   
    value = 5
    print("Local value:", value)
    print("Global value:", globals()['value'])
compare_with_global()

def greet(name="Guest"):
 print("Hello", name)
greet()
greet("John")

#ANS4 
def calculate_discount(price, discount_rate=0.10):
    discount = price * discount_rate
    final_price = price - discount
    return final_price
print("Final price:", calculate_discount(1000))
print("Final price with 20% discount:", calculate_discount(1000, 0.20))

#MINI PROJECT 
def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * (tip_percent / 100)
    return tip
bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
tip_amount = calculate_tip(bill, tip_percent)
print("Tip amount: ", round(tip_amount, 2))
