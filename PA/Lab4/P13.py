def cautare_cuvant(cuvant, *fisierein):
    for fisier in fisierein:
        with open(fisier) as f:
            found = False
            linie = 1
            x = f.readline().split()
            while len(x) > 0:
                if cuvant in x:
                    found = True
                    print("S-a gasit cuvantul ",cuvant," in fisierul ",fisier, " la linia ",linie)
                x=f.readline().split()
                linie+=1
            if not found:
                print("Nu s-a gasit cuvantul in fisierul",fisier)

cautare_cuvant("Ana","E:\PyCharmProjects\Lab4\cuvinte.txt","E:\PyCharmProjects\Lab4\cuvinteout.txt")