# Qn1- create a function that takes no parameters, uses arithmetic operators to calculate the area of the rectangle. Print the results.

def area():
 length=30
 width=20
 area=length * width
 print("The area of the rectangle is: ", area)
area() 

# Qn2-Functions with parameters
# create a function that accepts two numbers as parameters and returns their sum, difference,product and division.

def calculations(x , y):
 
 sum = x + y
 difference = x - y
 product = x * y
 division = x / y
 
 print("The sum of the two is: ", sum)
 print("The difference between the two is: ", difference)
 print("The product of the two is: ", product)
 print("The quotient of the two is: ", division)
calculations(10 , 5) 

# Qn3. Control statement (if...elif...else)
# Write a function that accepts a number(use input function),checks whether the  number is positive, negative or zero.

def number():
 number=int(input("Enter a number: "))

 if number==0:
  print("The number is zero")
 elif number > 0:
  print("The number is positive")
 else:
  print("The number is negative")

number()   

# Qn4. Loop with arithmetic.
# Write a function that accepts a number n, uses a loop and calculates the sum of numbers from 1 to n.
def sum_to_n(n):
 
  total_sum = 0
  for i in range(1, n + 1):
        total_sum += i
  print(f"The sum of numbers from 1 to {n} is:{total_sum} ")
  

n = int(input("Enter a number: "))
sum_to_n(n)

 # Qn5. While loop.
 # Write a function that accepts a number(use input function), uses a while loop and calculates the square of numbers from 1 upto that number.

def calculate_squares_until_n():
 number=int(input("Enter a number n:"))
 n = int(number)

 
 
 current_number=1

 print(f"Squares of numbers from 1 up to {n}:")

 while current_number <=n:
  square=current_number **2
  print(f"The square of {current_number} is {square}")
  
  current_number +=1 
  
calculate_squares_until_n() 





