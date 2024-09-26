# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "watermelon", "mango", "strawberry", "peach"]

# print(fruits[1:]) # adding a 0 gives apple, 1 gives orange, 2 gives banana, 3 gives coconut (just like strings)

# print(fruits[::2]) # this gives every second element in the list/string

# print(fruits[::-1]) # reverses the position of everything (apple goes to the end now, and peach goes to the start)

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits)) # gives you all the attributes for the list
# print(help(fruits))
# print(len(fruits)) # gives you the len of it
# print("apple" in fruits) # tells you the element of a list if its in there or not (like a boolean)

# fruits[0] = "pineapple" # this swaps the element/data/value in the list (changed apple into pineapple)
# fruits[-1] = "cherry" # changed peach into cherry
# print(fruits[0]) # prints the new swapped value
# print(fruits[-1])

# fruits[0] = "pineapple"
# fruits.append("pineapple") # adds an element to the end of the list
# fruits.remove("apple")
# fruits.insert(0, "pineapple") # doesn't replace just adds it between the elements in the list
# fruits.sort()
# fruits.reverse()
# fruits.clear()
print(fruits.index("apple"))

print(fruits)