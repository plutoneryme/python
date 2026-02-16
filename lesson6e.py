# On the try and except block: You run some codes/statements and if it is successful the try block will get executed otherwise the except block will be executed when there is an anticipated error.
try:
 number=100 
 answer=number/0

 print("The answer is: ",answer)
except Exception as e:
 print("There is an error: ",e) 

try:
 age=int(input("Enter your age: "))
 print("Next year you will be: ", age+1)
except Exception as e:
 print("There is an error: ",e) 

try:
 numbers=[10,20,30]
 print("The number is: ",numbers[5])
except Exception as e:
 print("There is an error: ",e) 

try:
 marks=int(input("Enter rhe marks:"))
 print("Your marks are: ",marks)
except ValueError as e:
 print("Invalid input! Please enter a number.") 
  

import math  
try:
 result=math.sqrt(-9)
 print("Result: ",result)
except ValueError as e:
 print("There is a valueError:",e)  
