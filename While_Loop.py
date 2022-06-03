i = 0
while(i < 10):
    print(i+1)
    i = i + 1


print("\nWhile loop with if and break statement")
i = 1
while(i <= 10):
    print(i)
    if i == 6:
        break
    i = i + 1

print("\nWhile loop with if and continue statement")
i = 1
while(i <= 10):
    i = i + 1
    if i == 6:
        continue
    print(i)
