fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(len(fruits))

movies = ["War", "My Name", "Conjuring", "Mom", "Dear Zindagi"]
for m in movies: 
  print(m)

nums = [5, 2, 9]
nums.append(7)
nums.sort()
print(nums)

#ANS 
numbers = [3,6,5,8,1,7,2,9]
numbers.sort()
numbers.append(4)
numbers.remove(9)
print(numbers)

names = ["Alice", "Bob", "Charlie"]
for name in names:
  if "a" in name.lower():
   print(name)

#ANS
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)

matrix = [[1,2,3], [4,5,6]]
print(matrix[1][2])

squares = [x*x for x in range(6)]
print(squares)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in matrix:
    for element in row:
        print(element)

#Mini Project
grocery_list = []

while True:
    print("\nChoose an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Print list")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print(f"{item} added to the list.")
    
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
    
    elif choice == "3":
        print("\nYour Grocery List:")
        for i, item in enumerate(grocery_list, start=1):
            print(f"{i}. {item}")
    
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
