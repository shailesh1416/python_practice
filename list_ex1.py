# datatypes
# string
# int
# float
# bool
# =================
# list
# =================
print("===================================")
item_list = ["banana","milk","tomato","milk","coconut oil"]
print(item_list)
# find length of list
print("length :",len(item_list))

# first item
print("First item :",item_list[0])

# last item
print("Last item :",item_list[-1])

# first 3 item
print("First 3 item :",item_list[0:3])

# adding an item in list
item_list.append("butter")
print(item_list)
item_list.append("grapes")
print(item_list)

# replacing a item
item_list[0]="Mango"
print(item_list)

#remove item from list
item_list.pop()
item_list.pop()
item_list.pop()
# item_list.pop(0)
print(item_list)

# inserting item

item_list.insert(0,"Apple")
item_list.insert(3,"watermelon")

print(item_list)

# list slicing

# print(item_list[-1:0:-1])

# item_list.clear()
# print(item_list)

print("count :",item_list.count('milk'))

# item_list.reverse()

print(item_list.index("Mango"))






