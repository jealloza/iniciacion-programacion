lista=[45,78,1,23,97,31,6]
elementos = len(lista)

for i in range(elementos):
    for j in range(elementos-i-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

for x in range(elementos):
    print(lista[x])