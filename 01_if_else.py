###
my_age = 19

# if
if my_age > 18:
    print("Adult")

# if else block
if my_age > 18:
    print("Adult")
else:
    print("Minor")

# if elif else
if my_age > 18:
    print("Adult")
elif my_age == 18:
    print("Turning adult")
else:
    print("Minor")

# code reduction
my_age = 16
msg = "Minor"
if my_age > 18:
    msg = "Adult"

print(msg)