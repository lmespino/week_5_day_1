# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "watermelon", "mango", "strawberry", "peach"]

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
# print(fruits.index("apple"))

# print(fruits)



# cars = ["Ford", "Volvo", "BMW"]

# add 4 new cars in the list
# cars.append("Honda")
# cars.append("Audi")
# cars.append("Chevrolet")
# cars.append("Cadillac")

# # print out the list of cars in an f-string
# # that says "The cars in the list are: "
# print(f"The cars in the list are: {cars}")

# # replace the last element in the list with "Toyota"
# # print out the list of cars in an f-string again
# cars[-1] = "Toyota"
# print(f"The cars in the list are: {cars}")

# # replace the 3rd element in the list with another car
# # print out the list of cars in an f-string
# cars[2] = "Ferrari"
# print(f"The cars in the list are: {cars}")

# # insert a new car in the 2nd position
# # print out the list of cars in an f-string
# cars.insert(1, "Porsche")
# print(f"The cars in the list are: {cars}")

# # remove the 3rd element from the list
# # print out the list of cars in an f-string
# cars.remove("Volvo")
# print(f"The cars in the list are: {cars}")

# # check if the list contains the car "Ford"
# # print out the result in an f-string
# print(f"Ford" in cars)

# for car in cars:
#     requestCar = input("Enter a car: ")
#     cars.append(requestCar)
#     print(f"The cars in the list are: {cars}")
#     if len(cars) >= 10:
#         print("You have reached the maximum number of cars")
#         break



# challenge
# create a list of friends
friends = ["Alejandro",]
print(friends)
# add 4 new friends in the list by requesting the user
# print out the list of friends in an f-string
for friend in friends:
    requestFriends = input("Enter a friend: ")
    friends.append(requestFriends)
    print(f"The friends in the list are: {friends}")
    if len(friends) >= 4:
        print("That's enough Friends")
        

# replace the last element in the list with another friend
# print out the list of friends in an f-string
friends[-1] = "Ramiro"
print(f"The friends in the list are: {friends}")

# replace the 3rd element in the list with another friend
# print out the list of friends in an f-string
friends[2] = "Joaquin"
print(f"The friends in the list are: {friends}")

# insert a new friend in the 2nd position
# print out the list of friends in an f-string
friends.insert(1, "Frida")
print(f"The friends in the list are: {friends}")