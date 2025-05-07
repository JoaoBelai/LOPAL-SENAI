def imc(peso, altura):
    imc = peso/(altura**2)
    return imc

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

print(imc(peso, altura))