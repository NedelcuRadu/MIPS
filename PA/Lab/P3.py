
f = open("E:\PyCharmProjects\Lab5\cuburi.txt")
g=open("E:\PyCharmProjects\Lab5\cuburi2.txt","w+")
cuburi = []  # (latura,culoare)
x = f.readline() # Scap de prima linie

for x in f:
    x = x.split()
    cuburi.append((int(x[0]), x[1]))

cuburi.sort(key=lambda x: -x[0])
print(cuburi)

cur=""
h=0

for x in cuburi:
    if x[1]!=cur:
        g.write("{} {} \n".format(*x))
        cur=x[1]
        h+=x[0]
g.write("\n")
g.write(f"Inaltime totala: {h}")