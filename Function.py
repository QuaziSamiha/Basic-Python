# function => a block of code

# ============= A function to print something =================
def greet():
    print("3 June, 2022")


greet()

# ======= A Function with parameters and return statement =========


def sum(a, b):
    c = a + b
    return c


print(sum(12, 10))

# ======= A Function with parameters and return statement =========


def sum2(a, b=10):
    c = a + b
    return c


print(sum2(22))
