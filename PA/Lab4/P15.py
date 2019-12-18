folositor=[]

def fisier_dict(nume_fisier):
    f = open(nume_fisier)
    x = f.readline().split()
    L = []
    while len(x) > 0:
        dict = {}
        dict["plecare"] = x[0]
        dict["sosire"] = x[2]
        dict["ora_plecare"] = x[3]
        dict["ora_sosire"] = x[4]
        L.append(dict)
        x = f.readline().split()
    return L


def timp_calatorie(ora_plecare, ora_sosire):
    x = ora_plecare.split(":")
    y = ora_sosire.split(":")
    r = [0, 0]
    r[0] = int(y[0]) - int(x[0])
    r[1] = int(y[1]) - int(x[1])
    if r[0] > 23 or r[1] > 59:
        print("Eroare")
        return None
    else:
        return r[0], r[1]


def DFSInit(dictionar_calatorie):
    viz = {}
    for x in dictionar_calatorie:
        viz[x] = 0
    return viz


def DFS(nod, dictionar_calatorie,viz):
    viz[nod] = 1
    folositor.append(nod)
    for vecin in dictionar_calatorie[nod]:
        if viz[vecin] == 0:
            DFS(vecin, dictionar_calatorie,viz)
    print(viz)


def calatorie(lista_program):
    dict = {}
    for x in lista_program:
        dict[x["plecare"]] = set()
        dict[x["sosire"]] = set()
    for x in lista_program:
        try:
            dict[x["sosire"]].add(x["plecare"])
            dict[x["plecare"]].add(x["sosire"])
        except KeyError:
            dict[x["sosire"]] = {x["plecare"]}
            dict[x["plecare"]] = {x["sosire"]}
    DFS("Brasov", dict,DFSInit(dict))


calatorie(fisier_dict("E:\PyCharmProjects\Lab4\\traseu.txt"))
print(folositor)