harryDict = {
    "Name": "Harry",
    "Class": "4th",
    "Marks": 34.56,
    "Hours In School": 6
}

print(harryDict)
print(harryDict["Marks"])

# ================Update item of Dictionary======================
harryDict["Marks"] = 78
print(harryDict["Marks"])

# ==========================Remove An Item======================
harryDict.pop("Hours In School")
print(harryDict)
