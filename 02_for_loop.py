##############
# for i in iterableObject:
    # print(i)

# for i in range(5):
#     print(i)
# for i in range(0,5):
#     print(i)
for i in range(0, 5, 1):
    print(i)

my_list = [10, 30, 20, 50, 50]
# get all elements
for each_element in my_list:
    print(each_element)

# get all elements and find it;s index
i = 0
for each_element in my_list:
    print(i, each_element)
    i += 1

# get value and index using enumerate
for i, val in enumerate(my_list):
    print(i, val)

# for loop in dict
my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender":"Male"
}

# accessing keys
for each_key in my_dict.keys():
    print(each_key)

# fetch value based on keys
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])

# fetch value and keys from items
for each_item in my_dict.items():
    print(each_item)