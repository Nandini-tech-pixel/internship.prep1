for i in range(1, 6):
   print("Hello", i)

for i in range(10, 0, -1):
    print(i)

count = 0
while count < 5:
  count += 1
  print("Counting", count)

for i in range(1, 6):
  for j in range(i):
   print("*", end="")
print() 
 
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    spaces = rows - i
    stars = i
    print(""*spaces + "*" *stars)

while True:
  word = input("Enter word: ")
  if word == "exit":
   break
print("You typed:", word)

#ANS
correct_password = "admin18"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

#Mini project
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
