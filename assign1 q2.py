
brandname=input("enter brandname:")
color=input("enter color:") 
car={brandname:color} 
f=open("carlist.txt","a")
#f.write(str(brandname)+" ")
#f.write(str(color)+" ")
#f.write(str(car)+" ")
f.write("brandname:"+brandname+" ")
f.write("color:"+color)
f.close()

print(car) 