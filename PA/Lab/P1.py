def afisare_timpi_servire(tis):
    sum=0
    sumtot=0
    print("Ordine Timp servire Timp mediu")
    for x in tis:
        sum+=x[1]
        sumtot+=sum
        print(x[0],x[1],sum)
    print(sumtot/len(tis))


f=open("E:\PyCharmProjects\Lab5\\tis.txt")
init=[(int(x))for x in f.readline().split()]

tis2=[(i,init[i-1]) for i in range(1,len(init)+1)]

print(tis2)
afisare_timpi_servire(tis2)
print()
afisare_timpi_servire(sorted(tis2,key=lambda x:x[1]))
