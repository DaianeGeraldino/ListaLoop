lista_compras = []
cont = True

while cont:
    usuario = input("Escreva o que deseja colocar na lista de compras ")
    lista_compras.append(usuario)

    condicao = int(input("Digite 1 para parar e 2 para continuar "))
    if condicao == 1:
        cont = False
    elif condicao == 2:
        cont = True

print(lista_compras)