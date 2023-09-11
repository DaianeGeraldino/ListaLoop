lista_um = []
lista_nova = []

while cont:
    usuario = int(input("Escreva os numeros deseja colocar na lista "))
    lista_um.append(usuario)

    condicao = int(input("Digite 1 para parar e 2 para continuar "))
    if condicao == 1:
        cont = False
    elif condicao == 2:
        cont = True



for i in lista_um:
    if i in lista_nova:
        continue
    else:
        lista_nova.append(i)

print(lista_nova)