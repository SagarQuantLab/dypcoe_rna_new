# STRING SLICING

my_string = "This is RnA Students"
            # ['T', 'h', 'i'...]
            #  0     1    2        -2  -1

# access first element
print(my_string[0])

# access second element
print(my_string[1])

# access 'This'
print(my_string[0:4])

# access 'Ti'
print(my_string[0:4:2])

# last letter
print(my_string[-1])

# second last letter
print(my_string[-2])

# reverse string
print(my_string[::-1])

# reverse 'Stundents'
print(my_string[:-9:-1])

# upper case/ lower case
print(my_string.upper())
print(my_string.lower())

# replace 's' with 'X'
print(my_string.replace("s", "X"))