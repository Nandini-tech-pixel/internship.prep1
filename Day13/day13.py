name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

#ANS1
price = 58.876
formatted_price = f"{price:.2f}"
print(formatted_price)

text = " Hello Python! "
print(text.strip().lower().replace("python", "World"))

#ANS2
def is_valid_email(email):
    return email.endswith('.com') and ' ' not in email
email = input("Enter your email: ")
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")

import re
email = "test@example.com"
match = re.match(r"\w+@\w+\.com", email)
print(match is not None)

import re
pattern = r"^\d{3}-\d{3}-\d{4}$"
phone = input("Enter phone number: ")
if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

import re
text = "The price is $45"
m = re.search(r"\$\d+", text)
print(m.group())

import re
text = "It's a #beautiful day to go #swimming."
hashtags = re.findall(r"#\w+", text)
print(hashtags)

#Mini project
import re
email = input("Enter your email: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print("Email is valid!")
else:
    print("Invalid email format.")
