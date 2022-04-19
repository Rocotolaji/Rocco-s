def num_ingredientes (p):
    print(len(p))
def gramos(p,i,j):
    print(p[i][j])
def costo_g(p,i,j):
    print(p[i][j])
huevo=["0","50","100","5000"]
aceite=["1","10","250","2500"]
sal=["2","1","1000","1000"]
jugo_de_limón=["3","5","300","1500"]
mayo = [huevo,aceite,sal,jugo_de_limón]
num_ingredientes(mayo)
gramos(mayo,1,1)
costo_g(mayo,2,2)
