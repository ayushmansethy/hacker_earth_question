tag = input()
vowel = ["A", "E", "I", "O", "U", "Y"]
tagarr = list(tag)
for x in tagarr:
    if x.isdigit():
        pass

    else:
        tagarr.remove(x)

tagarr = list(map(int, tagarr))
# print(tagarr)
if tag[2] not in vowel:
    if (tagarr[0]+tagarr[1])%2 ==0 and (tagarr[2]+tagarr[3])%2==0 and (tagarr[3]+tagarr[4])%2==0 and (tagarr[5]+tagarr[6])%2==0:
        print("valid")

    else:
        print("invalid")
else:
    print("invalid")
