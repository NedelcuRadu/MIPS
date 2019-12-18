def citire():
    n=int(input("N:"))
    L=[]
    for i in range(n):
        L.append(int(input("Valoare")))
    return L

def maimare(i,j,x,L):
    for z in range(i,j+1):
            if L[z]>x:
                return z
    return -1

L=citire()
ok=True
for i in range(len(L)-1):
    if maimare(i,i+1,L[i],L)!=-1:
        ok=False
        break

if ok:
    print("Da")
else:
    print("Nu")