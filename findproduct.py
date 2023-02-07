n=int(input())
arr=list(input().split(" "))

arr=list(map(int,arr))
def product(arr):
    prod =1
    for x in arr:
        prod = (prod*x)%((pow(10,9))+7)
    return prod
    
print(product(arr))
print(arr)