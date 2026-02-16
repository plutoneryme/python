# Loops - sometimes we may need to do a piece of work a number of repeated times and in such cases we may use loops.
# A loop is a control structure that allows us to execute a block of code repeatedly untill a certain condition is met .
# There are two types  of loops i.e for loop and while loop.
# below is the syntax for for loop in python
""""
for variable in range(n):
   #block of code to be executed
"""

# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")

for greeting in range(5):
 print("Hello Moses", greeting)

 print("============================================================")

 for number in range(10 , 20):
  print("number",number)

  print("============================================================")
  # find the even numbers in the range of 50 to 71.
  for number in range(50 , 71 , 2):
   print(number)

   print("============================================================")
   # create a python program that prints the odd numbers from 100 -150
   for number in range(101, 150, 2):
    print(number)

print("============================================================")
# create a program that prints the multiples of 3 starting from 201 to 150.

for number in range(201 , 149 ,-3):
 print(number)

print("============================================================")
# create a python program that prints the leap years in between 2000 t0 2024.
for year in range(2000 ,2025 ,4):
 print(year)

 # 2
 