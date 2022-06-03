s1 = {23, 2, 2, 2, 2, 2, 7, 3, 2, 2, 1, 2, 12, 7, 6, 3, 12}
print(s1)

# =====================Add an element in Set================
s1.add(55)
print("\nAdd an element in set : ")
print(s1)

# ====================Add Multiple element in Set==============
s1.update([12, 12, 423, 3423, 634, 123, 444, 23])
print("\nAdd Multiple element in Set : ")
print(s1)

# ======================Length of Set=====================
print("\nLength of Set : ")
print(len(s1))

# ===================Remove an element from Set===============
print("\nRemove an element from Set : ")
s1.remove(634)
# s1.remove(777) # it will show an error as this element not exist
print(s1)

s1.discard(777)  # this won't show any error
s1.discard(423)
print(s1)
