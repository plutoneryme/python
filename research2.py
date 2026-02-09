# the for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# the break statement in for loop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#    Example
# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  #while loop
  counter=1
  while counter<=10:
    print("counter")
    counter=counter+1