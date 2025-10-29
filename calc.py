def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
choice = input("""
Which function do you require?
               
Press "A" to add
Press "T" to take away
Press "M" to multiply
Press "D" to divide
""")

if choice in "A":
    print (f"Those numbers added together are", add(num1,num2))
if choice in "T":
    print (f"Those numbers taken away are", minus(num1,num2))
if choice in "M":
    print (f"Those numbers multiplied together are", multiply(num1,num2))
if choice in "D":
    print (f"Those numbers divided are", divide(num1,num2))

