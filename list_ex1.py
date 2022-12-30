# create an empty list by name basket
barket = []

# print empty basket
print("Fruit list : ",barket)

# take 10 input and append to basket
for i in range(5):
    # take user input
    f1 = input(f"Enter fruit {str(i+1)} : ")
    # store f1 in basket
    barket.append(f1)

# print the basket
print("Fruit list : ",barket)
print("Total fruits :",len(barket))