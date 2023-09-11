lista = []
min = 5
cont = True

while cont:
    palavras = input('Digite uma palavra ')

    if len(palavras) < min:
        print('Digite uma palavra com caracteres maior que 5 ')
    else:
        lista.append(palavras)

    resposta= int(input("Deseja adicionar uma nova palavra digite 1 para sim e 2 para não "))
    if resposta == 1:
        cont = True
    elif resposta == 2:
        cont = False

print(lista)