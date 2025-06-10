fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # first item
print(fruits[-1]) # last item
print(fruits[1]) #2nd item
print(fruits[2]) #last item
print(fruits[-2]) #2nd item
fruits.append("orange")
fruits.remove("banana")
fruits.insert(1, "kiwi")
print(fruits)
print("Length:", len(fruits))
hobbies = ["badminton","reading novels","cooking"]
hobbies.append("traveling")
hobbies.remove("reading novels")
hobbies.insert(1,"cycling")
print(hobbies)
dimensions = (1920, 1080)
print("Width:", dimensions[0])
colors = {"red", "green", "blue", "red"}
print(colors)
colors.add("yellow")
colors.remove("blue")
print(colors)
birthdate = (2005, "February" , 18)
print(birthdate)
print ("Month:", birthdate[1])
favouritemovies = {"Skyforce","Uri","Conjuring","Uri","War","Anabella"}
print(favouritemovies)
toggles = ["Alice", "Bob", "Charlie"]
for toggle in toggles:
    print("Hello",toggles[1])
for i in range(1,6):
    print("number:",i)
for letter in "Python":
    print(letter)
hobbies = ["badminton","reading novels","cooking"]
for hobbie in hobbies:
    print(hobbies)
for i in range(2,11,2):
    print(i)

counter = 0
while counter<5:
    print("Counter:",counter)
    counter+=1
Password = ""
while Password != "Secret":
    Password = input("Enter password:")
print("Access granted.")
for i in range(1,11):
    print(i)
i = 1     #using while loop
while i <= 10:
    print(i)
    i += 1

number = 3 
guess = 0 
while guess!= number:
    guess = int(input("Guess a number between 1 to 10:"))
print("Correct!")
numbers = [2, 4, 6, 8]
for num in numbers:
   print("Square:", num ** 2)

total = sum(numbers) # Average
print("Average:", total / len(numbers))

search_name = input("Enter name to search: ")
names = ["Alice", "Bob", "Eve"]
if search_name in names:
   print("Found")
else:
   print("Not found")
# Even numbers in the list
numbers = [2,4,6,8]    
even_count = 0
for num in numbers:
    if num%2==0:
        even_count+=1
print("Total even numbers:", even_count)
# Modify the search to be case sensitive
names = ["Saanvi", "sandeep", "suman", "Nandini"] 
search = input("Enter name: ")

for name in names:
    if name.lower() == search.lower():
        print("Name found!")
        break
else:
    print("Name not found.")
# A todo list app
tasks = []
while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Quit")
    choice = input("Choose option.")
    if choice == "1":
        task = input("Enter task:")
        tasks.append(task) 
        print("Total number of tasks after task added:", len(tasks))
    elif choice == "2":
        print("Your Tasks.")
        for t in tasks:
            print("-",t)
    elif choice == "3":
        print ("Goodbye!")
        break
    else:
        print("Invalid option")
