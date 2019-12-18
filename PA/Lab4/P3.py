def min_max(*args):
    if len(args) > 0:
        max = -1
        min = args[0]
        for x in args:
            if not isinstance(x, int) or x < 0:
                return None
            else:
                min = x if x < min else min
                max = x if x > max else max
        return min, max
    else:
        return None


try:
    f = open("E:\PyCharmProjects\Lab4\\numere.txt")
    g = open("E:\PyCharmProjects\Lab4\impartire.txt", "w")
    L = [int(x) for x in f.read().split()]
    L=min_max(*L)
except FileNotFoundError:
    print("Nu exista fisierul")
except ValueError:
    print("Nu sunt toate nr naturale")
except TypeError:
    print("Nu sunt toate nr naturale")
except ZeroDivisionError:
    print("Minimul este 0")
except Exception as e:
    print(e)
else:
    if L!=None:
        g.write(str(L[1] / L[0]))
    else:
        print("Nu sunt toate nr naturale")
    f.close()
    g.close()
