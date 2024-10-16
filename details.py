# request user's name
# request user's age
# request user's house number 
# request user's street
# use f string format to print out the information in one line.

name = input("Enter your name: ")
age = int(input("How old are you: "))
house_num = int(input("What is your number: "))
street = input("Enter your street name: ")
print(f" This is {name}, I am {age} years old. I live at house number {house_num} on {street}. ")