f = open("data.txt", "r")
print(f.read())
f.close()

file = open("myfile.txt", "w")  
file.write("First line\n")
file.write("Second line\n")
file.write("Third line\n")
file.close()

file = open("myfile.txt", "r")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print(line1)
print(line2)
print(line3)
file.close()

f = open("output.txt", "w")
f.write("Hello world\n")
f.close()

entry = input("Write today's journal: ")
file = open("journal.txt", "a")
file.write(entry + "\n")
file.close()
print("Saved!")

with open("log.txt", "r") as f:
 print(f.read())

file = open("myfile.txt", "r")
for line in file:
    print(line.upper())
file.close()

try:
 with open("nofile.txt", "r") as f:
   print(f.read())  
except FileNotFoundError:
 print("File not found!")

#Mini project
from datetime import date

entry = input("Write your log entry: ")
today = date.today()

file = open("log.txt", "a")
file.write(f"{today}: {entry}\n")
file.close()

print("Saved!")
