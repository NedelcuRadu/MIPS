def cmpValori(x, y):
    if x == y:
        return True
    return False


def cautare(x, L, cmpValori):
    for y in range(len(L) - 1, -1, -1):
        if cmpValori(L[y],x):
            return y
    return None


def cmp(Student):
    return Student[1], -Student[2]


L = [4, 4, 3, 1, 4]
print(cautare(4, L, cmpValori=cmpValori))
Student1 = ["Nume", 135, 4, "Promovat"]
Student2 = ["Nume2", 134, 2, "Nepromovat"]
# L.append(Student1)
# L.append(Student2)
# print(L)
# print(sorted(L, key=cmp))
