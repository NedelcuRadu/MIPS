def negative_pozitive(L):
    a=[]
    b=[]
    for x in L:
        a.append(x) if x>=0 else b.append(x)
    return b,a
g=open("E:\PyCharmProjects\Lab4\\numere.txt","a")
f=open("E:\PyCharmProjects\Lab4\\numere2.txt")
L=[int(x) for x in f.read().split()]
B=negative_pozitive(L)
g.writelines(str(B))

