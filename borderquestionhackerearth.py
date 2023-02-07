t = int(input())
maax = []
for z in range(t):
    temp = input().split(" ")
    n, m = list(map(int, temp))
    store = []
    for x in range(n):
        tems = input()
        store.append(tems.count("#"))
    maax.append(max(store))
    store.clear()
for x in maax:
    print(x)



       