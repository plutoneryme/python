#Tuple
#It is an immutable type of a list i.e it cannot change.
#To introduce a tuple we use parenthesis()

counties=("Nairobi","Mombasa","Nakuru","Eldoret","Kajiado","Kisii")
print(counties)
print(type(counties))

#slicing a tuple
print(counties[3:])

#Accessing items of a tuple by use of an index
print(counties[5])

#Note:below will generate an error
#attribute error
counties.append("Machakos")
print("This is the sixth county: ",counties)