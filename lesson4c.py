# A for loop can be used to iterate through a list, tuple, string or even a dictionary.

name="Sonia"

for letter in name:
 if letter=="n":
  print("This is letter n")
 else:
  print(letter) 

print("===================")
  # Below is a list of counties.
counties=["nairobi","machakos","nakuru","embu","meru","kisii","kajiado","eldoret"]

print(counties)

for county in counties:
 print(county)

print("===================")
for county in counties:
 if "nairobi" in counties:
  print("The county is part of the list")
  break
 else:
  print("The county is not part of the list") 

print("===================")

search=input("Enter a county to search:")

found=False # asume the list is empty at first.very important.
for county in counties:
 if county==search:
  found=True # update the found variable.
  break #stop checking once found.
 
if found:
 print(search,"is available")
else:
 print(search,"is not available")

 print("================")  

#  for loop can be used to iterate through a dictionary. 

player={
 "name":"mbappe",
 "age":25,
 "teams": ["PSG","Monaco","Barcelona"],
 "nationality":"french"

}

for key in player:
 print(key)
print("===================")

for value in player:
 print(player[value])

# print player name

print("===================")
# loop through the teams the player has played for.
for team in player ["teams"]:
 print(team)