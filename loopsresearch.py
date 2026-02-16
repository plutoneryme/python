# using enumerate- gives index + value.

names=["Ann","Ben","Cara"]

for index, name in enumerate(names):
 print(index, name)


 # nested for loops

for i in range(3):
 for j in range(2):
  print(i,j)

print("==========")
# looping through a list
name="sonia"
for letter in "sonia":
  print(letter)
print("==========")

x=1
while x <=5:
 print(x)
 x=x+1
print("==========")

# Break
for i in range(10):
 if i==5:
  break
 print(i)
print("==========")

# continue
for i in range(5):
 if i==2:
  continue
 print(i)
print("==========")
# pass- do nothing(placeholder)

for i in range(5):
 pass
print("==========")

# else with loops
for i in range(4):
 print(i)
else:
 print("loop finished completely!")
print("==========")
# But
for i in range(3):
 if i==1:
  break
else:
 print("This will not run")

# real life example

attempts=0
while attempts<3:
 password=input("enter password: ")
 if password=="admin123":
  print("Access granted")
  break
 attempts+=1
else:
 print("Too many attempts")  
 