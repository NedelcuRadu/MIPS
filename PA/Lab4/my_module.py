def citire():
    N = int(input("N:"))
    a = []
    for i in range(N):
        x = int(input("Valoare:"))
        a.append(x)
    return a


def afisare(v):
    for x in v:
        print(x, end=" ")
    print()


def valpoz(v):
    a = []
    for x in v:
        if x >= 0:
            a.append(x)
    return a


def semn(v):
    for i in range(len(v)):
        v[i]=v[i]*(-1)
