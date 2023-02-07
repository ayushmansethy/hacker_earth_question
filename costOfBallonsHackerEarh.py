T = int(input())
for x in range(T):
    cg, cp = [int(x)for x in input().split()]

    n = int(input())
    g = p = 0
    for x in range(n):
        q, t = [int(x)for x in input().split()]
        g += q
        p += t
    if (g*cg+p*cp) > (p*cg+g*cp):
        print(p*cg+g*cp)
    else:
        print(g*cg+p*cp)
