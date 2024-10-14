num=int(input("Enter a start point : "))
end=int(input("Enter a end point : "))
for num in range(num,end+1):
    if num>1:
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
         print(num)