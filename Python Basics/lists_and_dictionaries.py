# def user_info(name, age=30, city="Cairo"):
#     """This function prints name, age and city from an argument provided to the function."""
#     print("{} is {} years old, from {}".format(name, age, city))
#
#
# user_info("Abdullah", 29, "Riyadh")
# user_info("Abdullah")
#
#

# fruits = ["peaches", "apples", "pears"]
#
# years = [3, "1995", 2.5, 987, "1994"]
#
# fruits.append("oranges")
# print(fruits)
#
# fruits.extend(years)
# print(fruits)


stuff = {"food": 15, "energy": 100, "enemies": 3}


# print the value using pass the key
print(stuff.get("food"))

# print the all items in the dictionary key and value
print(stuff.items())

# print all key in the dictionary
print(stuff.keys())

# remove the item from the dictionary and will remove the last item in the dictionary
print(stuff.popitem())

# set default value for the spcific key in the dictionary
print(stuff.setdefault("food"))

# also can add a new key and value to the dictionary using setdefault
print(stuff.setdefault("friends", 120))

# use update to update the dictionary using another dictionary
new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

