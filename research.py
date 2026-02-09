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


# nested if
# if outer_condition:
#     # Executes if outer_condition is True
#     if inner_condition:
#         # Executes only if BOTH conditions are True
#         print("Both conditions met")
#     else:
#         # Executes if outer is True but inner is False
#         print("Outer met, inner failed")
# else:
#     print("Outer condition failed")


age = 30
is_member = True

if age > 18:
    # This block runs if the person is an adult
    if is_member:
        print("Ticket price is $12.") # Both are True
    else:
        print("Ticket price is $20.") # Adult but not a member
else:
    # This block runs if the person is not an adult
    if is_member:
        print("Ticket price is $8.")  # Minor and a member
    else:
        print("Ticket price is $10.") # Minor and not a member


password="python123"
User_name="plutone"
is_active=True

if User_name:
   if password: 
       if is_active:
        print("Is logged in")
       else:
        print("account is not active") 
   else:
      print("password required")   
else:
 print("username required")   

password = (input("Enter password: "))
User_name = (input("Enter Username: "))





