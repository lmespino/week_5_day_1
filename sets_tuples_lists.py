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



# # challenge
# # create a list of friends
# friends = ["Alejandro",]
# print(friends)
# # add 4 new friends in the list by requesting the user
# # print out the list of friends in an f-string
# for friend in friends:
#     requestFriends = input("Enter a friend: ")
#     friends.append(requestFriends)
#     print(f"The friends in the list are: {friends}")
#     if len(friends) >= 4:
#         print("That's enough Friends")
        

# # replace the last element in the list with another friend
# # print out the list of friends in an f-string
# friends[-1] = "Ramiro"
# print(f"The friends in the list are: {friends}")

# # replace the 3rd element in the list with another friend
# # print out the list of friends in an f-string
# friends[2] = "Joaquin"
# print(f"The friends in the list are: {friends}")

# # insert a new friend in the 2nd position
# # print out the list of friends in an f-string
# friends.insert(1, "Frida")
# print(f"The friends in the list are: {friends}")

##############sets################
# sets are unordered and unindexed
# they are defined using curly brackets
# they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) # gives you all of the attributes/methods that can be used with sets
# print(help(fruits)) # documentation/methods that can be used with sets
# print(len(fruits)) # number of elements in the set
# print("volvo" in fruits) # check if an element is in the set
# add an element to the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
# add multiple elements to the set
# print(fruits.update(["orange", "kiwi", "pineapple"]))
# print(fruits)
# print(fruits.pop()) # removes the last element in a set
# print(fruits)
# print(fruits.clear()) # clears the set
# print(fruits)
# when do we want to use sets?
# sets are useful when you want to store a collection of items that should not be changed. and you do not care about the order of the items.
# example: a collection of unique items
# social_security_numbers = {123456789, 987654321, 123456789}
# remove the last element in this set
# social_security_numbers.pop()
# print(social_security_numbers)
# add another social security number
# social_security_numbers.add(345678901)
# print(social_security_numbers)
# social_security_numbers.add(456789012)
# print(social_security_numbers)

################tuples#################
# touples are immutable and are defined using parantheses
# create a tuple called my_tuple with the following values
# example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(example_tuple)
# print(example_tuple.count(2)) # count the number of times the value 2 appears in the tuple
# print(dir(example_tuple)) # attributes that can be used with tuples
# print(help(example_tuple)) # documentation/methods that can be used with tuples
# print(len(example_tuple)) # number of elements in the tuple
# print(2 in example_tuple) # check if an element is in the tuple
# When are tuples useful?
# Tuples are useful when you want to store a collection of items that should not be changed, such as days of the week, monnths of the year, etc.
# if you want to find the index of a value in a tuple
# print(example_tuple.index(2))
# lymeric = "peter pipe picked a peck of pickled peppers"
# convert the string into a tuple
# split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# find how many times the word peck appears in the tuple
# print(lymeric_tuple.count())

# loops with tuples
# for item in example_tuple:
#     print(item)
#     break

#################dictionary####################
# dictionaries are unordered, changeable and indexed
# they are defined using curly brackets
# they have keys and values
# a collection of {key:value} pairs, no duplicates
# keys are unique
# values can be of any data type
capitals = {"Kenya":"Nairobi", 
            "Uganda":"Kampala", 
            "Tanzania":"Dodoma",
            "Rwanda":"Kigali",
            "China":"Beijing",
            "USA":"Washington DC"}
print(capitals)
print(dir(capitals)) # attributes that can be used with dictionaries
print(help(capitals)) # documentation/methods that can be used with dictionaries
print(len(capitals)) # number of items in the dictionary
# if you want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get["Kenya"])
# add an item to the dictionary two ways
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
# add three more countries and their capitals to the dictionary
capitals.update({"France":"Paris", "Germany":"Berlin", "Italy":"Rome"})

capitals.pop("China") # Remove an item from the dictionary
print(capitals)
# clear the dictionary
# capitals.clear() # do not run this
# loop through the dictionary to get the keys
for key in capitals:
    print(f"these are the {key}")

# print the values in the dictionary
items_all = capitals.items() # key value pairs
for key, value in items_all:
    print(f"{key} is the capital of {value}")