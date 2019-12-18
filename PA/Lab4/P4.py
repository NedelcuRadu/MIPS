def check_prim(n):
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prim_gen():
    yield 2
    n = 3
    yield n
    while (True):
        n += 2
        if check_prim(n):
            yield n


N = int(input("N="))
gena = prim_gen()
for i in range(N):
    print(next(gena), end=" ")

print()
genb = prim_gen()
x = next(genb)
while x < N:
    print(x,end=" ")
    x = next(genb)
