#Python lists
#A list in python is a collection of items that are ordered in a certain way.
#A list is introduced using the square brackets[].
#The items of a list are stored inside indexes. Note:in programming we start counting from index zero(0). 
#A list is mutable i.e the contents of a list can be changed.

cars=["BMW","Benz","Hiance","Prado","Probox","Mc laren","Range"]
print(cars)
print(type(cars))


#Accessing items of a list
print(cars[2])
print("The car on index four is: ",cars[4])


#list slicing- this is creating a list from a given bigger list.
print(cars[4:])
 #printing from index 0-3
print(cars[:4])

#print from hiance to probox.
print(cars[2:5])

#list- mutability
#We use the function append to add an item at the end of a list.
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

#We use the pop function to remove an item at the end of a list.
cars.pop()
print(cars)

#we can use an index to add items to a list.
cars[5] = "Pajero"
print(cars)

#we can use the sort function to sort our items in alphabetical order.
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


cars.pop(4)
print(cars)

del cars[4]
print(cars)

cars.remove("BMW")
print(cars)


