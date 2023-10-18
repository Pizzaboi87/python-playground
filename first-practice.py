# 01 Example

name = None
age = None
temp = None

while not name:
  name = input("What is your name?: ")

print("Hello " + name)

# 02 Example

while not age:
  age = input("\nHow old are you?: ")
age = int(age)

if age == 100:
  print("Wow! You are a century years old.")
elif age > 100:
  print("Hmm... Are you in the Guiness World Records as well?")
elif age >= 18:
  print("Ok, so you are an adult.")
elif age < 0:
  print("Hmm... It seems you haven't been born yet.")
else: 
  print("Ok, then you are a child.")

# 03 Example

while not temp:
  temp = input("\nWhat is temperature?: ")
temp = int(temp)

if (temp < -30 or temp > 50):
  print("Are you still alive?")
elif not(temp >= 0 and temp <= 30):
  print("The weather is bad today. :(")
else:
  print("The weather is good today. :)")