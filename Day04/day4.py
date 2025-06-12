#Ans 1
full_name = "Nandini Singh"
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
#Ans2
name = "Nandini Singh"
vowels = "aeiouAEIOU"
count = 0
for char in name:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
#Ans3
sentence = "My name is Nandini."
reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)
#Ans4 
sentence = input("Enter a sentence: ")
word = input("Enter a word to count: ")
count = sentence.lower().count(word.lower()) 
print(f"The word '{word}' appears {count} time(s) in the sentence.")
#Ans5 
text = "Hockey is the national sport of India."
new_text = text.replace(" ", "-")
print(new_text)
#Ans6
text = input("Enter a string: ")
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
#Ans7
email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Domain name:", domain)
#Ans8 
name = input("Enter your name: ")
num = input("Enter your favorite number: ")
print(f"Hello {name}, your favorite number is {num}.")

#Mini project
name = input("Enter a name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
activity = input("Enter an activity: ")
feeling = input("Enter a feeling: ")

story = f"""
Once upon a time, there was a man named {name}, he owned a {animal}.They lived together in a small house in {place}.
{name} loved his {animal} a lot, he would take it for a {activity} everyday. Both of them were quite {feeling} together
and the {animal} loved {name}'s company. People in their locality also loved their bond."""
print(story)

#Mini project 2 
def chatbot():
    responses ={
        "hi": "Hello! 👋",
        "hello": "Hi there!",
        "how are you": "I'm doing good.",
        "what's your name": "I'm ChatBot, your virtual friend",
        "bye": "Goodbye! 👋 Take care!",}
    

    print("🤖 ChatBot: Hello! Type something (or 'exit' to quit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("ChatBot: Chat ended. 👋")
            break
        reply = responses.get(user_input, "Sorry, I don't understand that. 😅")
        print("ChatBot:", reply)
chatbot()
