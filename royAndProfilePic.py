l=int(input())
n=int(input())
for x in range(n):
    temp=list(input().split(" "))
    w,h=list(map(int,temp))
    if w<l and h<l:
        print("UPLOAD ANOTHER")
    else:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")