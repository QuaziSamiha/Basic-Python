lst = [61, 2, 3, 4, 6, 41]  # an object of list class
print(lst)
# list is an orderable or chageable collection
var = type(lst)
print(var)

# ===========access a signle element within list===============
var = lst[0]
print(var)

# ================access a finite range within list===============
print("\nAccess a finite range within List : ")
var = lst[1:4]
print(var)

# ==============change element in list==========================
print("\nChange Element of a specific index : ")
print(lst)
lst[2] = 45
print(lst)
print("\nAccess a finite range within List : ")
var = lst[1:4]
print(var)

# ---------------length of string-----------------------------
print("\nUse of len keyword to find length : ")
print(len(lst))

# ==================Add element end of the list================
print("\nUse of append() function : ")
lst.append(100)
print(lst)

# =================Add element to a specific index======================
print("\nUse of insert() function : ")
lst.insert(1, 233)
print(lst)

# ===============Remove an element==============================
print("\nUse of remove() function : ")
lst.remove(41)
print(lst)

# ===============Remove last elemetn from list====================
print("\nUse of pop() function : ")
lst.pop()
print(lst)

# ===============Remove an element of specific index============
print("\nUse of del keyword : ")
del lst[3]
print(lst)

# =================Clear a List========================
print("\nUse of clear() function : ")
lst.clear()
print(lst)
