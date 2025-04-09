#------------Exercício 1----------
print("\nExercício 1")

idade = int(input("Digite sua idade:"))

if idade < 18:
    print("\nVocê é menor de idade!")
else:
    print("\nVocê é maior de idade!")

#---------------------------------
#------------Exercício 2----------
print("\nExercício 2")

nota = float(input("\nDigite a nota do aluno:"))

if nota >= 9:
    print("\nNota excelente!")
elif nota >= 7:
    print("\nNota boa!")
elif nota >= 5:
    print("\nNota na média!")
else:
    print("\nNota insuficiente!")

#---------------------------------
#------------Exercício 3----------
print("\nExercício 3")

numero = int(input("Digite um número:"))

if numero % 2 == 0:
    print("\nO número é par")
else:
    print("\nO número é ímpar")

if numero % 3 == 0:
    print("\nO número é múltiplo de 3!")
else:
    print("\nO número não é múltiplo de 3!")

if numero % 5 == 0:
    print("\nO número é múltiplo de 5!")
else:
    print("\nO número não é múltiplo de 5!")

#---------------------------------
#------------Exercício 4----------
print("\nExercício 4")

valor1 = float(input("\nEscreva o primeiro número:"))
valor2 = float(input("\nEscreva o segundo número:"))

if valor1 == valor2:
    print("\nOs valores são iguais")
elif valor1 > valor2:
    print("\nO primeiro número é maior que o segundo!")
else:
    print("\nO segundo número é maior que o primeiro!")

#---------------------------------
#------------Exercício 5----------
print("\nExercício 5")

idade = int(input("Digite a idade:"))

if idade < 2:
    print("\nBebê")
elif idade < 13:
    print("\nCriança")
elif idade < 18:
    print("\nAdolescente")
elif idade < 60:
    print("\nAdulto")
else:
    print("\nIdoso")

#---------------------------------
#------------Exercício 6----------
print("\nExercício 6")

print("\n1.Celcius para Fahrenheit")
print("\n2.Fahrenheit para Celcius")
verificador = int(input("\nDigite o número do que você gostaria de converter:"))

temperatura = float(input("\nQuantos graus?"))

if verificador == 1:
    temperatura = temperatura*1.8 + 32
    print(f"\nA temperatura é {temperatura}°F")
elif verificador == 2:
    temperatura = (temperatura-32)/1.8
    print(f"\nA temperatura é {temperatura}°C")
else:
    print("\nVocê não escolheu uma opção válida")

#---------------------------------
#------------Exercício 7----------
print("\nExercício 7")

lado1 = float(input("\nEscreva o valor do primeiro lado:"))
lado2 = float(input("\nEscreva o valor do segundo lado:"))
lado3 = float(input("\nEscreva o valor do terceiro lado:"))

if (lado1 + lado2 > lado3) and (lado3+ lado2 > lado1) and (lado1+lado3 > lado2):
    print("\nÉ um triângulo válido!")
    if lado1 == lado2 == lado3:
        print("\nÉ um triângulo equilátero")
    elif lado1 != lado2 != lado3 != lado1:
        print("\nÉ um triângulo escaleno")
    else:
        print("\nÉ um triângulo isóceles")
else:
    print("\nNão é um triângulo válido!")

#---------------------------------
#------------Exercício 8----------
print("\nExercício 8")

idade = int(input("Digite sua idade:"))

renda = float(input("Digite sua renda:"))

if (idade >= 18) and(renda > 1500):
    print("\nVocê pode sim pegar um epréstimo pois você é um adulto e ganha mais de R$1.500,00 por mês")
elif (idade < 18) and(renda > 1000):
    print("\nVocê pode sim pegar um epréstimo pois você tem menos de 18 anos e ganha mais de R$1.000,00 por mês")
else:
    print("\nVocê não pode pegar um empréstimo")

#---------------------------------
#------------Exercício 9----------
print("\nExercício 9")

import random

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

usuario = input("Você quer jogar Pedra, Papel ou Tesoura?").upper()

computador = random.choice(opcoes)

print(f"\nO computador escolheu: {computador}")
print(f"\nVocê escolheu: {usuario}")

if (computador == "PEDRA" and usuario == "TESOURA") or (computador == "TESOURA" and usuario == "PAPEL") or (computador == "PAPEL" and usuario == "PEDRA"):
    print("\nO computador ganhou!")
elif (usuario == "TESOURA" and computador == "PAPEL") or (usuario == "PAPEL" and computador == "PEDRA") or (usuario == "PEDRA" and computador == "TESOURA"):
    print("\nVocê ganhou!")
elif usuario == computador:
    print("\nEmpate")
else:
    print("\nEscolha inválida!")





