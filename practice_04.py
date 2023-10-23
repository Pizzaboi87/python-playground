#Random
import random

x = random.randint(1,6)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)
print(cards)


#Exceptions
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers please!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)


#File detection
import os

path="./test.txt"

if os.path.exists(path):
    print("That location exists.")
    if(os.path.isfile(path)):
        print("That is a file.")
    elif(os.path.isdir(path)):
        print("That is a directory.")
else:
    print("That location doesn't exist.")


#Read a file
path_to_read="./test.txt"

try:
    with open(path_to_read) as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")


#Write a file
text = "This is a new example test.\nThis will be in the new file,\nHopefully\n"

with open('new_file.txt', 'w') as file:
    file.write(text)

append_text = "\nThis text will follow the previous one."

with open('new_file.txt', 'a') as file:
    file.write(append_text)


