import math
a=int(input("Enter the first coefficient: "))
b=int(input("Enter the second coefficient: "))
c=int(input("Enter the third coefficient: "))
disc=(b**2 - (4*a*c))
if disc>0:
    root1= (-b+math.sqrt(disc))/(2*a)
    root2= (-b-math.sqrt(disc))/(2*a)
    print("Root 1 : ",root1)
    print("Root 2 : ",root2)
elif disc==0:
    root1= -b/(2*a)
    print("Root 1 : ",root1)
else:
    real_part= -b/(2*a)
    imaginary_part= (math.sqrt(abs(disc)))/(2*a)
    print("Root 1 : ",real_part," + ",imaginary_part,"i")
    print("Root 2 : ",real_part," - ",imaginary_part,"i")