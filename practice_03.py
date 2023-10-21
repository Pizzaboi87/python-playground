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


#Args
def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(addition(1,2,3,4,5))


#Kwargs
def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Ms.", first_name="Rahel", middle_name="Anna", last_name="Temesvari")


#Format method
animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))
print("The {prop1} jumped over the {prop2}".format(prop1="dog", prop2="doghouse"))


#Format method with positioning
print("The result of the test is a(n) {result:<9} for Carlos.".format(result='"A"'))
print("The result of the test is a(n) {result:>9} for Peter.".format(result='"C"'))
print("The result of the test is a(n) {result:^9} for Putty.".format(result='"B'))


#Format method with numbers
PI = 3.14159
number = 1000

print("The PI to two decimal places: {:.2f}".format(PI))
print("The number with comma: {:,}".format(number))
print("The number in binary: {:b}".format(number))
print("The number in octo: {:o}".format(number))
print("The number in hexa: {:X}".format(number))
print("The number in scientific: {:E}".format(number))