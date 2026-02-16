# python functions.
# They are a block of code/statements that performs a given task/action.They can be reused throughout the program to perform different tasks.
# Functions are defined using the def keyword.(define).
# We have two main types of functions i.e
# 1.  In-built functions -theu come preinstalled with the intepreter i.e print(),pop(),range(),append()....
# 2.   User-defined functions- they are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the function body,it is usually indented and to invoke a function we use the function name.


def greetings():
 print("Hello, how are you?")

# below we call the function by use of it's name.
greetings()

print("==========")

# Addition function.
def addition():
 num1=40
 num2=50
 sum=num1+num2
 print("Th sum of the number is : ", sum)
addition() 

print("==========")
# create a function that is able to multiply three values.

def multiplication():
 num1=3
 num2=4
 num3=2
 product=num1*num2*num3
 print("The product is: ",product)
multiplication()

print("==========")
# below is a division function.
def divide():
 number1=int(input("Enter the first number:"))
 number2=int(input("Enter the second number:"))
 quotient = number1/number2
 print("The quotient is: ", quotient)
divide() 

print("------------")
for function in range(3):
 divide()
 

