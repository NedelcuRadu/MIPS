f = open("E:\PyCharmProjects\Lab5\\bani.txt")
g = open("E:\PyCharmProjects\Lab5\plata.txt", "w")

banc = [int(x) for x in f.readline().split()]
banc.sort(reverse=True)
print(banc)

val = int(f.readline())
g.write(f"{val} = ")
i = 0
while val > 0:
    k = val // banc[i]
    if k > 0:
        val -= banc[i] * k
        g.write(f" {banc[i]}*{k} ")
        if val > 0:
            g.write("+")
    i += 1
