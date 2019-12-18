f = open("E:\PyCharmProjects\Lab5\proiecte.txt")
proiecte = []
nume=[]
profit=[]
maxi = 0
for x in f:
    x = x.split()
    maxi = max(maxi, int(x[1]))
    proiecte.append((x[0], int(x[1]), int(x[2])))  # Nume, Termen, Profit
proiecte.sort(key=lambda x: -x[2])
print(proiecte)
T = 0
i=0
print(maxi)
while T < maxi and i<len(proiecte):
    if proiecte[i][1]>=T:
        nume.append(proiecte[i][0])
        profit.append(proiecte[i][2])
        T+=1
    i+=1
print("Proiecte: ",*nume)
print("Profit: ",*profit)