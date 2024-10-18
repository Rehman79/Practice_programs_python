num=int(input("Enter the terms : "))
a=0
b=1
count=0
if num<=0:
    print("Enter positive value for terms : ")
elif num==1:
    print(num)
else:
    while count<num:
     print(a)
     temp=a+b
     a=b
     b=temp
     count+=1