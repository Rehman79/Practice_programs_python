num=int(input("Enter a number : "))
type_num=str(num)
len_num=len(type_num)
temp_num=num
sum=0
while temp_num>0:
    result=temp_num%10
    sum=sum+result**len_num
    temp_num=temp_num//10
if sum==num:
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong Number")