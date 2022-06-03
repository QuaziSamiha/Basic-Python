variable = input("Wheather is 'Rainy' or 'Sunny' or 'Snowy' : ")

if variable.lower() == "rainy":
    print("Today is rainy day")
elif variable.lower() == "sunny":
    print("Today is sunny day")
elif variable.lower() == "snowy":
    print("Today is snowy day")
else:
    print("Sorry, I'm not sure about that")


secret_number = '3'
guess = input("Enter a secret number between (1 to 5) : ")

if guess.isdigit() == False:
    print("Number should be only digit")
elif guess == '1':
    print("Guess is too low")
elif guess == '2':
    print("Guess is not correct")
elif guess == '3':
    print("Guess is correct")
elif guess == '4':
    print("Guess is not correct")
elif guess == '5':
    print("Guess is too high")
else:
    print("Guess is out of range")