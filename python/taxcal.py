

    
print("ENTER Salary IN INR------------------\n")
m1= float(input("INR  "))

totalm=m1
if totalm<150000:
    print("No Tax")
    
    print("NET TAX PAYBlE 0")
elif totalm<=300000 and totalm>=150001:
    print("10% tax")
    sal=m1*10/100
    print("Tax Return Of => ")
    print(sal)
elif totalm<=500000 and totalm>=300001:
    print(" 20% Tax")
    sal=m1*20/100
    print("Tax Return Of => ")
    print(sal)
elif  totalm>=500001:
    print("30% Tax")
    sal=m1*30/100
    print("Tax Return Of => ")
    print(sal)


