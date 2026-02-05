#A dictionary is a data type that stores data in terms of key-value pair.
#It is introduced by the use of curly braces.
#The values stored inside of a dictionary can be of any data type.
#To access the values in adictionary, we use the keys.


phonebook={
 "Benson":"2547432233",
 "Mary": "2547672233",
 "Stephen": "2547434533"

}
#showing the entire phonebook
print(phonebook)
print(type(phonebook))

#Printing out benson's number
print(phonebook["Benson"])

print("=====================================")

player={
 "name":"Messi",
 "age": 40,
 "teams":["PSG","Barcelona","Argentina"]

}

print(player["teams"][1])

player ["age"] = 39
print(player)