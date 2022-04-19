numero=input("escriba numero binario: ")
ceros=0
unos=0
for j in numero:
    if j=="0":
        ceros=ceros+1
print(ceros)
for k in numero:
    if k=="1":
        unos=unos+1
print(unos)
ceros_q="0"
unos_q="1"
print(ceros_q*ceros,unos_q*unos)
