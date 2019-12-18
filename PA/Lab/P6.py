f = open("E:\PyCharmProjects\Lab5\spectacoleP6.txt")
g = open("E:\PyCharmProjects\Lab5\spectacoleP6out.txt", "w+")

evenimente=[]
for x in f:
    evenimente.append((x[:5], x[6:11], x[12].replace("\n",""))) # (Ora de inceput, Ora final, Nume)

evenimente.sort()

print(evenimente)
dict={}
cur="24"
sali=0
for x in evenimente:
    if x[0]<cur:
        sali+=1
        cur = min(cur,x[1])

g.write(f"{sali} sali \n")
cur="0"
k=1
for x in evenimente:
    if x[0]>cur:
        dict.setdefault(k,[]).append(x)
        cur=max(cur,x[1])
    else:
        k+=1
print(dict.items())
