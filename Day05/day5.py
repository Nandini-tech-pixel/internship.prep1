age = int(input("Enter your age:"))
if age >= 18:
   print("You can vote!")
else:
   print("Too young to vote.")
#Ans 1
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

score = int(input("Enter marks:"))
if score >= 90:
  print("Grade A")
elif score >= 75:
  print("Grade B")
elif score >= 50:
  print("Grade C")
else:
  print("Fail")

#Ans2 
marks = float(input("Enter the score (0-100): "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 90:
    print("Grade: B")
elif 50 <= marks < 75:
    print("Grade: C")
elif 0 <= marks < 50:
    print("Grade: F")
else:
    print("Invalid score")

#and, or, not 
username = "admin"
password = "1234"
u = input("Username: ")
p = input("Password: ")
if u == username and p == password:
  print("Access granted")
else:
  print("Access denied")

#Ans 3
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

secret = 7
guess = int(input("Guess a number (1-10): "))
if guess == secret:
  print("Correct!")
elif guess < secret:
  print("Too low")
else:
  print("Too high")

#Ans 4
secret_number = 7
chances = 0
while chances < 3:
    guess = int(input("Guess the number (between 1 and 10): "))  
    if guess == secret_number:
        print(" Correct! You guessed it!")
        break
    else:
        print("Wrong guess. Try again.")   
    chances += 1
    if chances == 3 and guess != secret_number:
     print("Sorry, you've used all your chances. The number was", secret_number)

#Mini project
correct_username = "admin"
correct_password = "1234"
attempts = 0
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("You are now logged in! Welcome,", username)
        break
    else:
        print("Incorrect username or password. Try again.")
        attempts += 1
    if attempts == 3:
       print("Multiple failed attempts. Access denied.")
