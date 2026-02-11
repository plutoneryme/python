#Nested if statements
# Is an if statement that s contained inside another statement.

age = 20
weight = 46

if age > 15:
 if weight > 50:
  print("you can donate blood")
 else:
  print("you cannot donate blood because of your weight")
else:
 print("you cannot donate blood because of your age")   