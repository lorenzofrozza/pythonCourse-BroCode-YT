#List [] = mutable, most flexible

# fruits = ["Apple", "Orange", "Banana", "Strawberry"]
# # print(fruits[0])
# # print(fruits[3])
# fruits[0] = "Pineapple"
# fruits.append("Mango")
# fruits.remove("Orange")
# fruits.pop(0) # remove by index
# # fruits.clear()
#
# for fruit in fruits:
#     print(fruit, end=" ")


# Tuple () = immutable, faster

# fruits = ("Apple", "Orange", "Banana", "Strawberry")


# Set{} = mutable (add/remove), unordered, No duplicates, best for membership testing

fruits = {"apple", "orange", "banana", "strawberry", "strawberry", "strawberry"}
fruits.add("mango")
fruits.remove("apple")
fruit = input("Enter a fruit to search for: ")

for fruit in fruits:
     print(fruit, end=" ")

if fruit in fruits:
    print(f"\n{fruit} was found")
else:
    print(f"\n{fruit} was not found")


