try:
 x = 5 / 0
except ZeroDivisionError:
 print("Division by zero not allowed.")

#Ans 1
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")


try:
 x = int(input("Enter number: "))
except ValueError:
 print("Invalid input")
else:
 print("Number:", x)

#Ans 2
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That was not a valid integer.")

age = int(input("Enter age: "))
if age < 0:
 raise ValueError("Age cant be negative")

#Ans 3
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password is too short. It must be at least 8 characters long.")
    else:
        print("Password is valid!")
try:
    pwd = input("Enter your password: ")
    validate_password(pwd)
except ValueError as e:
    print("Error:", e)

try:
 with open("sample.txt") as f:
  print(f.read())
except FileNotFoundError:
 print("No file!")
finally:
 print("Done!")

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Cleanup complete. Program ended.")

#Mini project

def divide_numbers():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Thank you for using the calculator!")
divide_numbers()
