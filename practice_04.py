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


#Copy a file
import shutil

shutil.copyfile("test.txt", "copy/copy.txt")


#Move a file
import os

source = "test.txt"
destination = "copy/copy.txt"

try:
    if os.path.exists(destination):
        print(source + " is already there.")
    else:
        os.replace(source, destination)
        print(source + " was moved successfully.")
except FileNotFoundError:
    print(source + " was not found.")


#Delete a file
import os

path = "test.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print(path + " was not found.")
except PermissionError:
    print("You don't have permission.")
else:
    print(path + " was successfully deleted.")


#Delete an empty folder
import os

empty_folder = "empty_folder"

try:
    os.rmdir(empty_folder)
except FileNotFoundError:
    print(empty_folder + " was not found.")
except PermissionError:
    print("You don't have permission.")
except OSError:
    print("The folder is not empty, you can't use this function.")
else:
    print(empty_folder + " was successfully deleted.")


#Delete a folder with data
import shutil

folder_with_data = "folder_with_data"

try:
    shutil.rmtree(folder_with_data)
except FileNotFoundError:
    print(folder_with_data + " was not found.")
except PermissionError:
    print("You don't have permission.")
except OSError:
    print("The folder is not empty, you can't use this function.")
else:
    print(folder_with_data + " was successfully deleted.")
