def afisare(spectacol):
    g.write("{}-{} {}".format(*spectacol))


f = open("E:\PyCharmProjects\Lab5\spectacole.txt")
g=open("E:\PyCharmProjects\Lab5\spectacole2.txt","w+")
spec = []
for x in f:
    spec.append((x[:5], x[6:11], x[12:]))

spec.sort(key=lambda x: x[1])
print(spec)

cur = "0"
for i in range(0, len(spec)):
    if spec[i][0] >= cur:
        afisare(spec[i])
        cur = spec[i][1]
