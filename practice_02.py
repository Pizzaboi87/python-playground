# Nested loop
rows = int(input("How many rows?: "))
cols = int(input("How many cols?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()


# Loop Control Statements
# break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# continue
phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# pass
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)


# List
food = ["hamburger", "hotdog", "spaghetti", "lasagne"]

food[0] = "pizza"
food.append("ice cream")
food.remove("hotdog")
food.insert(0, "cake")
food.pop()
food.sort()

for i in food:
    print(i)


# 2D List
dinner = ["hamburger", "hotdog", "spaghetti"]
drink = ["cola", "coffee", "water"]
dessert = ["ice cream", "cake"]

food_list = [dinner, drink, dessert]

print(food_list[1][2])


# Set
utensils = {"knife", "fork", "spoon"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")

dinner_table = utensils.union(dishes)

for i in dinner_table:
    print(i)

print(utensils.intersection(dishes))
