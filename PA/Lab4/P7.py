def cmp1(x):
    return len(x), x


def cmp2(x):
    global L
    i = 0
    while (i < len(L)):
        if L[i] == x:
            break
        i+=1
    return len(x), i


f = open("E:\PyCharmProjects\Lab4\cuvinte.txt")
g = open("E:\PyCharmProjects\Lab4\cuvinteout.txt", "w")

L = f.read().split()
print(L)
print(sorted(L, reverse=True))
print(sorted(L, key=cmp1))
print(sorted(L, key=cmp2))
