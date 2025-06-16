#Tuples
coords = (4, 5)
print(coords[0])

birth_date = (18,2,2005)
print("Day:", birth_date[0])
print("Month:", birth_date[1])
print("Year:", birth_date[2])

#SETS
nums = {1, 2, 2, 3}
print(nums)
nums.add(4)
print(3 in nums)

names = set()
for i in range(5):
    name = input("Enter a name: ")
    names.add(name)
print("Unique names:")
for n in names:
    print(n)

#Dictionaries
student = {"name": "Alice", "age": 20}
print(student["name"])
student["age"] = 21

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92}
print("Students with marks greater than 80:")
for name, marks in students.items():
    if marks > 80:
        print(name, "-", marks)

students = {"Alice": 90, "Bob": 75}
for name, score in students.items():
  print(name, "scored", score)


Students = { 
    "Nandini": 93,
    "Saanvi": 90,
    "Adwita": 91,
    "Bhumi": 72,
    "Vaishnavi": 83
}

print("Students who scored above 85:")
for name, marks in Students.items():
    if marks > 85:
        print(name, "-", marks)

#Mini project
students = {}

while True:
    print("\n--- Student Dictionary System ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name to add: ")
        if name in students:
            print("Student already exists.")
        else:
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
