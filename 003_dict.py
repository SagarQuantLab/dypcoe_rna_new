# DICT
# {}, Keys, no duplicates, ordered, mutable

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender":"Male",
    "Name": "Sohan"
}

# access 'Rohan'
print(my_dict['Name']) 

#  print dict
print(my_dict)

# modified age to 25
my_dict["Age"] = 25
print(my_dict)

###########################################################################
# ITEM    ORDERED     DUPLICATES     MUTABLE     CALLED    SYMBOL
# LIST      Y              Y            Y         Index     []
# DICT      Y              N            Y          Keys     {}
# TUPLE     Y              Y            N          Index    ()
# SETS      N              N            N           -       {}