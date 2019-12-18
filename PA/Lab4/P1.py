from math import sqrt


def ipotenuza(a, b):
    return sqrt(a ** 2 + b ** 2)


b = int(input("B="))
found = False
for a in range(1, b + 1):
    c = ipotenuza(a, b)
    if c == int(c):
        print(a, b, int(c))
        found = True

if not found:
    print("Nu exista triplete")
