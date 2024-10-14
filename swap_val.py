a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("First Number : ",a,"Second Number : ",b)
a,b=b,a
print("First Number : ",a,"Second Number : ",b)

print("Other approach")
print("First Number : ",a,"Second Number : ",b)
a=a+b
b=a-b
a=a-b
print("First Number : ",a,"Second Number : ",b)