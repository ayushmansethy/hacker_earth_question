temp=input().split(" ")
l,r,k=list(map(int,temp))
count =0
for x in range(l,r+1):
    if x%k ==0:
        count +=1
    else:
        pass
print(count)