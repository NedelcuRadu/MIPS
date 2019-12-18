from math import pi


def lungime_arie_cerc(r):
    return pi * r ** 2, 2 * pi * r


r = int(input("R="))
print(*lungime_arie_cerc(r))
