num=int(input("Enter a starting range number : "))
num2=int(input("Enter a ending range number : "))
for i in range(num,num2+1):
    len_num = len(str(i))
    sum = 0
    temp_num = i

    while temp_num>0:
        result=temp_num%10
        sum=sum+result**len_num
        temp_num=temp_num//10
    if i==sum:
        print(i)