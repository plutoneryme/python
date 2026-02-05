#how if statement works
number=15
if number >10 :
 print("This number is positive")


#you can have multiple statements inside a block

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

  #using variables in conditions.

  is_logged_in = True
if is_logged_in:
  print("Welcome back!")

  #if... else statement
  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  #elif statement
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a != b:
  print("a and b are not equal")
else:
  print("a is greater than b")

  #shorthand if
  #one line if statement
  a = 5
b = 2
if a > b: print("a is greater than b")