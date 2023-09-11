lista = []
cont = True

while cont:
    usuario = int(input("Escreva os numeros deseja colocar na lista "))
    lista.append(usuario)

    condicao = int(input("Digite 1 para parar e 2 para continuar "))
    if condicao == 1:
        cont = False
    elif condicao == 2:
        cont = True

print(f'O maior numero é', max(lista))
print(f'O menor numero é', min(lista))