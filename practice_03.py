#Dictionary
capitals = {
    "Hungary": "Budapest",
    "Greece": "Athens",
    "Spain": "Madrid",
    "Germany": "Berlin",
    "Russia": "Moscow"
}

capitals.update({"Italy": "Rome"})
capitals.pop("Russia")

print(capitals["Spain"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print("------------")

for key, value in capitals.items():
    print(key + " - " + value)

#Function
def test_function(first_name, last_name, age = 36):
    print ("Hello " + first_name + " " + last_name + "!")
    print ("You are " + str(age) + " years old.")

name_first = "Peter"
name_last = "Weiser"
test_function(name_first, name_last)
print("-.-.-.-.-.-")
test_function("Carlos", "Nunez", 33)

def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 8))