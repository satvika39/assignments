import math
num1=abs(int(input("enter first value")))
num2=abs(int(input("enter second value")))
num3=abs(int(input("enter third value")))
num4=abs(int(input("enter four value")))
num5=abs(int(input("enter five value")))
Total=num1+num2+num3+num4+num5
f=open("pro1.txt","a")
f.write(str(num1)+" ")
f.write(str(num2)+" ")
f.write(str(num3)+" ")
f.write(str(num4)+" ")
f.write(str(num5)+" ")
f.write(str(Total)+" ")
f.close()
print("the sum of those values are",Total)

