num=int(input("Enter a number : "))
result=1
if num<0:
    print("Factorial doesn't exist")
elif num==0:
    Print("Factorial : 1")
else:
    for i in range(1, num + 1):
        result = result * i
print(f"Factorial : {result}")