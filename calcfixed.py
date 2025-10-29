def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


while True:
    try:
        num1 = int(input("Enter number 1: "))
        break
    except ValueError:
        print("Please enter a valid integer for number 1.")

while True:
    try:
        num2 = int(input("Enter number 2: "))
        break
    except ValueError:
        print("Please enter a valid integer for number 2.")
        
choice = input("""
Which function do you require?
               
Press "A" to add
Press "T" to take away
Press "M" to multiply
Press "D" to divide
""").strip().upper()

if choice in ("A"):
    print (f"Those numbers added together are", add(num1,num2))
elif choice in ("T"):
    print (f"Those numbers taken away are", minus(num1,num2))
elif choice in ("M"):
    print (f"Those numbers multiplied together are", multiply(num1,num2))
elif choice in ("D"):
    print (f"Those numbers divided are", divide(num1,num2))
else:
    print("Invalid choice. Please select A, T, M, or D.")

