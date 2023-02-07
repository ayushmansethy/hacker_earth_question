D=int(input())
oc,of,od=list(map(int,input().split(" ")))
cs,cb,cm,cd=list(map(int,input().split(" ")))
cost_of_classic=(oc*of)+((D-of)*od)
cs=D/cs
cost_of_onlinetaxi=cb+(cs*cm)+cd*D
if cost_of_onlinetaxi<cost_of_classic or cost_of_classic==cost_of_onlinetaxi:
    print("Online Taxi")
else:
    print("Classic Taxi")


