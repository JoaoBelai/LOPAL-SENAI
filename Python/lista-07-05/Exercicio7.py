def regressivo(num):
    print(num)
    if num == 1:
       print("Fim")
    else:
        regressivo(num-1)

numero = int(input("Digite de qual número você deseja começar a contagem regressiva: "))

regressivo(numero)