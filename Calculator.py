def multiply(a, b):
    return float(int(a) * int(b))
def addition(a,b):
    return float(int(a) + int(b))
def subtraction(a,b):
    return float(int(a) - int(b))
def division(a,b):
    return float(int(a) / int(b))
x = input("Give out the first number: ")
y = input("Give out the second number: ")
operation = input("Select operation(*,/,+,-)")
if operation == '*':
    print(multiply(x,y))
if operation == '/':
    print(x, " divided by ", y, ":", division(x,y))
if operation == '+':
    print(addition(x,y))
if operation == '-':
    print(subtraction(x,y))
