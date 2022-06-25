# ------------------------------string--------------------------
name = "Harry"
print(name)

# ------------------multiline string----------------------------
'''
#  will show an error to write multiline string within double qoute
name = "Code 
with harry"

'''

# use 3 single qoutes to use multiline string
name = '''Code
with harry
'''
print(name)

# --------------------------string index--------------------------------------
name = "Harry"
print(name[0])
print(name[1:4])
# start from index 1 and go before index 4 that means index 3
print(name[2:5])


# -------------------string with space & without space--------------------------
name = "    Harry   "
print(name)
print(name.strip())

# --------------------length of string----------------------
name = "Harry"
print(len(name))

# -------------------built-in function for string-------------------
var = name.lower()
print(var)
var = name.upper()
print(var)
var = name.replace("r", "t")
print(var)
var = name.replace("ar", "t")
print(var)

name = "Harry, Pattty, Marty"
print(name.replace(", ", "\n"))  # comma & space is replaced by new line
print(name.replace(",", " "))  # comma is replaced by white space

# --------------------concatenation of string------------------------------
str1 = "This is a "
str2 = "practice"
print(str1 + str2)

name1 = "Harry"
name2 = "Rohan"
temp = "This is a {} and his friend name is {}".format(name1, name2)
print(temp)

# by default
temp = "This is a {0} and his friend name is {1}".format(name1, name2)
print(temp)

# customized
temp = "This is a {1} and his friend name is {0}".format(name1, name2)
print(temp)

temp = f"this is {name1} and his friend is {name2}"
print(temp)
