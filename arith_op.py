a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))
print('Choose operation to perform:')
print('1. +')
print('2. -')
print('3. /')
print('4. *')
print('5. **')
op = input("Enter the operation number: ")

match op:
    case '1':
        print(a + b)
    case '2':
        print(a - b)
    case '3' if b>0:
        print(f"{a / b}:.2f")
    case '4':
        print(a * b)
    case '5':
        print(a ** b)
    case _ if b==0:
        print("Cannot divide by zero")
    case _:
        print("Invalid operation chosen")
