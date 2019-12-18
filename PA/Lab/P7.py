f=open("E:\PyCharmProjects\Lab5\obiecte.txt")
g=open("E:\PyCharmProjects\Lab5\obiecteout.txt","w+")
obiecte=int(f.readline())
obj=[]
for x in range(obiecte):
    obi=f.readline().split()
    obj.append((int(obi[0]),int(obi[1]), 0)) # (Valoare, greutate, fractie)
G=int(f.readline())

obj.sort(key=lambda x:x[1]/x[0])
print(obj)
i=0
valoare=0
g.write("Greutate:\n")
g.write(f"{G} = ")
while G>0:
    if i<=len(obj):
        if obj[i][1]<=G:
            G-=obj[i][1]
            valoare+=obj[i][0]
            obj[i]=(obj[i][0],obj[i][1],1)
            i+=1
        else:
            f=G/obj[i][1]
            valoare+=obj[i][0]*f
            G=0
            obj[i]=(obj[i][0],obj[i][1],f)
    else:
        G=0

for x in obj:
    if x[2]==1:
        g.write(f" {x[1]} +")
    else:
        g.write(f"{f:.2f}*{x[1]} ")
g.write("\n")
g.write("\n")

g.write("Valoare obiecte din rucsac:\n")
for x in obj:
    if x[2]==1:
        g.write(f" {x[0]} +")
    else:
        g.write(f" {f:.2f}*{x[0]} ")

g.write(f"= {valoare}")
