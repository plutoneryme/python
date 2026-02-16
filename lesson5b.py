# Functions with parameters.
# Parameters are values that get passed as arguments given to a function inside of the parenthesis.


def greeting(name):
 print(f"{name} How are you ,hope everything is fine.")
greeting("Sonia") 
greeting("Jacob")
greeting("Amos")

print("==============")
def message(names):
 print(f"Hello {names}. We shall be having a general meeting on date...Please avail yourself")
message("Alex") 
message("Dan")
message("Alison")
message("Mike")

# def greeting(name):
#  print("How are you ,hope everything is fine.", name)
# greeting("Sonia") 

# create a function that accepts parameters to add two numbers.

def addition(x , y):
 sum= x+y
 print("The sum of the numbers is: ",sum)
addition(45 , 45)


