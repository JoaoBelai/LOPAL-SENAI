# ------ Exemplo 1 ------
def dobro(num):
    result = num * 2
    return result

numero = float(input("Digite um número: "))

print(f"O dobro do número {numero} é: {dobro(numero)}")

# ------ Exemplo 2 ------
def maior(num1, num2):
    if num1 > num2:
        print(f"O {num1} é o maior número!")
    elif num1 < num2:
        print(f"O {num2} é o maior número!")
    else:
        print("Os números são iguais")


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

maior(numero1, numero2)

# ------ Exemplo 3 ------
def media(qtd):
    lista = []
    for i in range(qtd):
        numero = float(input(f"Escreva o {i+1}° número: "))
        lista.append(numero)
        i+=1

    soma = sum(lista)
    media = soma/qtd

    return media

quantidade = int(input("Digite quantos serão os números para a média: "))

print(media(quantidade))

