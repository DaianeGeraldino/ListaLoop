lista_um = [ 2, 5, 6, 7, 8, 12]
lista_dois = [2, 6, 4, 5, 12, 8]
lista_iguais = []

for i in range(6):
    if lista_um[i] in lista_dois:
        lista_iguais.append(lista_um[i])

print(lista_iguais)
