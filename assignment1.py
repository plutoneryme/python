#Assignment
#1. Write a python program that is able to calculate the BMI of a person whose weight is 78kgs and height is 1.75 meters = (weight)/(height squared)
# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
#search and come up with an example of a complex data type


weight = 78
height = 1.75
BMI = (weight)/(height**2)
print ("This is the BMI: ", BMI)


# 2. Find the Area and perimeter of a rectangle whose length is 48cm and width is 25cm
length = 48
width = 25
area = length * width
print("This is the area: ", area)

perimeter=(2*length)+(2*width)
print("This is the perimeter: ", perimeter)


#list data type
fruits=["apple","banana","mango","banana"]
print(fruits[2])
fruits.append("orange")
print(fruits[1])

#tuple data type
coordinates=(10,20)
print(coordinates[1])

#dictionary data type
student={
    "name":"Sonia",
    "age": 18,
    "grade":"A"
}
#print the dictionary
print(student)
#print the dictionary item
print(student["age"])
#ammend
student["age"]=20
print(student)









"""This is a module-level docstring."""

def my_function(a, b):
    """
    Adds two numbers.

    Parameters:
      a (int): The first number.
      b (int): The second number.

    Returns:
      int: The sum of a and b.
    """
    return a + b
print(my_function.__doc__)
