def afisare():
    nume = input("Numele angajatului:")
    for angajat in Angajati:
        if angajat["nume"] == nume:
            print(*angajat)
            return


def salariumax(Angajati):
    max = 0
    for angajat in Angajati:
        if angajat["salariu"] > max:
            max = angajat["salariu"]
    return max


def salariumediu(Angajati):
    S = 0
    for angajat in Angajati:
        S += angajat["salariu"]
    return S / len(Angajati)


def alfabeticnume(Angajati):
    return sorted(Angajati, key=lambda angajat: angajat["nume"])


def pcte(Angajati):
    return sorted(Angajati, key=lambda x: (-x["varsta"], x["nume"]))


def pctf(Angajati):
    return sorted(Angajati, key=lambda angajat: (-angajat["salariu"], angajat["varsta"]))


f = open("E:\PyCharmProjects\Lab4\\angajati.txt")
x = f.readline().split(",")
Angajati = []
while len(x) > 1:
    print(x)
    angajat = {}
    angajat["nume"] = x[0]
    angajat["varsta"] = int(x[1])
    angajat["salariu"] = int(x[2])
    Angajati.append(angajat)
    x = f.readline().split(",")

print(pctf(Angajati))
print(Angajati)
