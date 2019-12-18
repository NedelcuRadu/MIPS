f = open("E:\PyCharmProjects\Lab5\\activitati.txt")
g = open("E:\PyCharmProjects\Lab5\intarzieri.txt", "w+")
x = f.readline()
activitati = []
for x in f:
    x = x.split()
    activitati.append((int(x[0]), int(x[1])))  # (duarata, termen limita)
print(activitati)
activitati.sort(key=lambda x: x[1])
print(activitati)

T = 0
g.write("Interval  Termen  Intarziere \n")

for x in activitati:
    g.write(f"({T}->{T + x[0]})      {x[1]}       {max(0, T + x[0] - x[1])} \n")
    T+=x[0]
