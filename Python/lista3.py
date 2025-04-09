#-------- Exercício 1 --------
print("\nExercício 1")
ano = int(input("\nInsira o ano a ser testado:"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"\nO ano {ano} é bissexto")
else:
    print(f"\nO ano {ano} não é bissexto")
#-----------------------------
#-------- Exercício 2 --------
print("\nExercício 2")
peso = float(input("\nInsira o seu peso em kg:"))
altura = float(input("\nInsira sua altura em m:"))

imc = peso/(altura**2)
print(f"\nSeu IMC é {imc:.2f}")

if imc < 18.5:
    print("\nBaixo Peso")
elif imc < 25:
    print("\nNormal")
elif imc < 30:
    print("\nSobrepeso")
elif imc < 35:
    print("\nObesidade")
elif imc < 40:
    print("\nObesidade Mórbida I")
else:
    print("\nObesidade Mórbida II")
#-----------------------------
#-------- Exercício 3 --------
print("\nExercício 3")
qtd = int(input("\nQuanto produtos você deseja comprar?"))
preco = float(input("\nQual o valor de cada produto?"))

valor_total = qtd*preco

if qtd > 100:
    desconto = valor_total * 0.9
    unidade_desc = desconto/qtd
    print(f"\nValor inicial do produto: {preco}")
    print(f"\nQuantidade de unidades do produto: {qtd}")
    print(f"\nValor de desconto por unidade: {unidade_desc}")
    print(f"\nValor total a pagar: {desconto}")
else:
    desconto = valor_total * 0.95
    unidade_desc = desconto / qtd
    print(f"\nValor inicial do produto: {preco}")
    print(f"\nQuantidade de unidades do produto: {qtd}")
    print(f"\nValor de desconto por unidade: {unidade_desc}")
    print(f"\nValor total a pagar: {desconto}")
#-----------------------------
#-------- Exercício 4 --------
print("\nExercício 4")

idade = int(input("\nDigite sua idade:"))

if idade < 16:
    print(f"\nVocê não pode votar porque tem apenas {idade} anos")
elif (idade < 18) or (idade >= 70):
    print(f"\nSeu voto é facultativo pois tem {idade} anos")
else:
    print(f"\nSeu voto é obrigatório pois você tem {idade} anos")
#-----------------------------
#-------- Exercício 5 --------
print("\nExercício 5")

idade1 = int(input("\nDigite a primeira idade:"))
idade2 = int(input("\nDigite a segunda idade:"))
idade3 = int(input("\nDigite a terceira idade:"))

if idade1 > idade2 and idade1 > idade3:
    print(f"\nA maior idade é: {idade1}")
elif idade2 > idade1 and idade2 > idade3:
    print(f"\nA maior idade é: {idade2}")
else:
    print(f"\nA maior idade é: {idade3}")

if idade1 < idade2 and idade1 < idade3:
    print(f"\nA menor idade é: {idade1}")
elif idade2 < idade1 and idade2 < idade3:
    print(f"\nA menor idade é: {idade2}")
else:
    print(f"\nA menor idade é: {idade3}")
#-----------------------------
#-------- Exercício 6 --------
print("\nExercício 6")
hora = int(input("\nDigite a hora:"))
minuto = int(input("\nDigite o minuto:"))
segundo = int(input("\nDigite o segundo:"))

print(f"\nA hora é: {hora}:{minuto}:{segundo}")

if hora >= 0 and hora <=24:
    print("\nA hora é válida!")
else:
    print("\nA hora é inválida!")

if minuto >= 0 and minuto <=60:
    print("\nO minuto é válido!")
else:
    print("\nO minuto é inválido!")

if segundo >= 0 and segundo <=60:
    print("\nO segundo é válido!")
else:
    print("\nO segundo é inválido!")
#-----------------------------
#-------- Exercício 7 --------
print("\nExercício 7")

nota = float(input("\nInsira a nota:"))

if nota >= 0 and nota < 3:
    print("\n Nota E")
elif nota < 5:
    print("\n Nota D")
elif nota < 7:
    print("\n Nota C")
elif nota < 9:
    print("\n Nota B")
elif nota <= 10:
    print("\n Nota A")
else:
    print("\nValor inválido")
#-----------------------------
#-------- Exercício 8 --------
print("\nExercício 8")

lado1 = float(input("\nInsira o valor do primeiro lado:"))
lado2 = float(input("\nInsira o valor do segundo lado:"))
lado3 = float(input("\nInsira o valor do terceiro lado:"))
lado4 = float(input("\nInsira o valor do quarto lado:"))

if(lado1 == lado2 and lado1 == lado3 and lado1 == lado4):
    print("\nÉ um quadrado")
elif (lado1 == lado2 and lado3 == lado4) or (lado1 == lado3 and lado2 == lado4) or (lado1 == lado4 and lado2 == lado3):
    print("\nÉ um retângulo")
else:
    print("\nNão é nenhum dos dois")
#-----------------------------
#-------- Exercício 9 --------
print("\nExercício 9")
num1 = float(input("\nInsira o valor do primeiro número:"))
num2 = float(input("\nInsira o valor do segundo número:"))

operacao = input("\n1.Para Soma (+)"
                 "\n2.Para Subtração (-)"
                 "\n3.Para Multiplicação (*)"
                 "\n4.Para Divisão (/)"
                 "\nDigite o número da operação:")

if operacao == "1":
    resultado = num1+num2
    print(f"\nO resultado é: {resultado}")
elif operacao == "2":
    resultado = num1-num2
    print(f"\nO resultado é: {resultado}")
elif operacao == "3":
    resultado = num1*num2
    print(f"\nO resultado é: {resultado}")
elif operacao == "4":
    resultado = num1/num2
    print(f"\nO resultado é: {resultado}")
else:
    print("Operação inválida")
#-----------------------------
#-------- Exercício 10 --------
print("\nExercício 10")

nota1 = int(input("\nDigite a primeira nota:"))
nota2 = int(input("\nDigite a segunda nota:"))
nota3 = int(input("\nDigite a terceira nota:"))

soma = nota1+nota2+nota3

if nota1 < nota2 and nota1 < nota3:
    soma = soma - nota1
    media = soma/2
    print(f"\nA média é: {media}")
elif nota2 < nota1 and nota2 < nota3:
    soma = soma - nota2
    media = soma / 2
    print(f"\nA média é: {media}")
else:
    soma = soma - nota3
    media = soma / 2
    print(f"\nA média é: {media}")
#-----------------------------
#-------- Desafio ------------
print("\nDesafio")

import random

numero = random.randint(1, 10)

usuario = int(input("\nAdvinhe o número de 1 a 10:"))

if numero == usuario:
    print(f"\nAcertou! O computador escolheu: {numero}")
elif numero > usuario:
    print("\nErrado mas você tem mais uma chance!")
    print(f"\nDica o número é maior que {usuario}")
    usuario = int(input(f"\nAdvinhe o número de 1 a 10:"))
    if numero == usuario:
        print(f"\nAcertou! O computador escolheu: {numero}")
    else:
        print(f"\nErrou! O número era: {numero}")
elif numero < usuario:
    print("\nErrado mas você tem mais uma chance!")
    print(f"\nDica o número é menor que {usuario}")
    usuario = int(input(f"\nAdvinhe o número de 1 a 10:"))
    if numero == usuario:
        print(f"\nAcertou! O computador escolheu: {numero}")
    else:
        print(f"\nErrou! O número era: {numero}")