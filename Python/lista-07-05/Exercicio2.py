def maior(qtd):
    maximo = 0
    for i in range(qtd):
        numero = float(input(f"Digite o {i+1}° número: "))

        if numero > maximo:
            maximo = numero
        i += 1
    print(f"O maior número é: {maximo}")

quantidade = int(input("Digite quantos números você quer verificar: "))

maior(quantidade)