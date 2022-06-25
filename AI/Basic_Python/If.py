age = 18
age = input("Enter Your Age: \n")
print(type(age))
age = int(age)
print(type(age))

if(age > 18):
    print("You can drive a car")
elif(age == 18):
    print("You are an awesome teen")
else:
    print("You cannot drive")
