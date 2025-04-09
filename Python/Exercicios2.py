#------------ Exercicio 1 -------------
numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))

media = (numero1+numero2+numero3)/3

print(f"A média é: {media:.2f}")
#--------------------------------------
#------------ Exercicio 2 -------------
prestacao = float(input("\nDigite o valor da prestação:"))

valor_final= prestacao + (10*prestacao/100)

print(f"O valor a ser pago é: {valor_final:.2f}")
#--------------------------------------
#------------ Exercicio 3 -------------
numero_ponderado1 = int(input("\nDigite o primeiro número:"))
numero_ponderado2 = int(input("Digite o segundo número:"))
numero_ponderado3 = int(input("Digite o terceiro número:"))

peso_ponderado1 = int(input("Digite o peso do primeiro número:"))
peso_ponderado2 = int(input("Digite o peso do segundo número:"))
peso_ponderado3 = int(input("Digite o peso do terceiro número:"))

pesos_somados = (numero_ponderado1*peso_ponderado1) + (numero_ponderado2*peso_ponderado2) + (numero_ponderado3*peso_ponderado3)

media_ponderada = pesos_somados/(peso_ponderado1+peso_ponderado2+peso_ponderado3)

print(f"A média ponderada é: {media_ponderada:.2f}")
#--------------------------------------
#------------ Exercicio 4 -------------
a = 5
b = 10

print(f"\n{a==b}") #False
print(f"\n{a!=b}") #True
print(f"\n{a>b}") #False
print(f"\n{a>=b}") #False
print(f"\n{a<b}") #True
print(f"\n{a<=b}") #True
#--------------------------------------
#------------ Exercicio 5 -------------
numero4 = int(input("\nDigite um número inteiro:"))

print(f"O número é positivo! {numero4>=0}")
print(f"O número é negativo! {numero4<0}")
#--------------------------------------
#------------ Exercicio 6 -------------

multiplo = int(input("\nDigite um número:"))

resto= multiplo%5

print(f"O número é multiplo de 5! {resto==0}")