print("Billing\n")

n=int(input("\nEnter Quatity Taken => "))
v=float(input("\nEnter Price => "))
d=float(input("\nDicount any => "))
t= float(input("\nEnter The Tax => "))

print("Net Price => ")
print(float(n*v))
netprice=float(n*v)
taxp=netprice*t/100
totalprice=netprice-(taxp*d/100)
tdiscount=(taxp*d/100)
print("discount Applied => ")
print(tdiscount)
print ("Tax implied => %")
print(t)


print("Total price => ")
print(totalprice)



