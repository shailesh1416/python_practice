# string
# int
# float
# bool
# list
# ===============
# dictionary{}
# ===============

person = {"name":"Shailesh","age":24,"address":"Boisar"}

# printing dictionary
print(person)
print()

# check data type
print(type(person))
print()

# accessing values using key
print(person["name"])
print(person.get("age"))
print()

# getting dictionary items
print("Items: ",person.items())

# printing dictionary keys
print(person.keys())
print()

# printing dictionary values
print(person.values())
print()

# total items in dictionary
print("Length od dictionary : ",len(person))
print()

# adding new item to dictionary
person["school"] = "CTES"
print(person)
print()

# adding using update
person.update({"color":"Blue"})
print(person)
print()

# upading a value
person["age"] = 23
print(person)
print()

# updateing using update method
person.update({"age":20})
print(person)
print()

# removing an item from dictionary
person.pop("color")
print(person)
print()

# removed last inserted item
person.popitem()
print(person)
print()

# clear the disctionary
person.clear()
print(person)