array = []
 
flag=False
n = int(input("Enter number of elements : "))
beg=1
loc=-1
end=n
mid=(beg+end)//2
for i in range(0, n):
	ele = int(input())

	array.append(ele) 
	
print(array)
 
item = int(input(" Enter the value you want to search: "))
 
while beg<=end:
    if array[mid]==item:
        loc=mid
        flag=True
        break
    
    elif array[mid]<item:
        beg=mid+1
        
    else:
        end=mid-1
       
    mid=(beg+end)//2
    
if flag==True:
    print("element Fount at\n")
    print(loc)
elif flag==False:
    print("Element not Found")
