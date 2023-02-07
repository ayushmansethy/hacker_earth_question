n = int(input())
data = input().split()
fino=[]
for  x in data:
   fino.append(x[-1])
print("Yes") if fino[-1] == "0" else print("no")