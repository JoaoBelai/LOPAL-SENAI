#------------ Exercicio 1 -------------
numero1 = float(input("\nInsira um número:"))
numero2 = float(input("\nInsira o segundo número:"))

resultado = numero1+numero2
print(f"\nO valor dos números somados é: {resultado:.2f}")
#--------------------------------------
#------------ Exercicio 2 -------------
impar = float(input("\nInsira um número, iremos testar se ele é ímpar:"))

resto = impar%2

print(f"\nO número é ímpar! {resto!=0}")
#--------------------------------------
#------------ Exercicio 3 -------------
valor1 = float(input("\nInsira o primeiro número:"))
valor2 = float(input("\nInsira o segundo número:"))

print(f"\nO primeiro número é maior que 3! {valor1>3}")
print(f"\nO segundo número é menor que 4! {valor2<4}")
#--------------------------------------
#------------ Exercicio 4 -------------
absoluto = float(input("\nInsira o valor para mostrarmos o valor absoluto:"))

absoluto = abs(absoluto)

print(f"\nO valor absoluto é: {absoluto:.2f}")
#--------------------------------------
#------------ Exercicio 5 -------------
par1 = int(input("\nInsira um número:"))
par2 = int(input("\nInsira o segundo número:"))

resto1 = par1%2
resto2 = par2%2

print(f"\nO primeiro número é par! {resto1==0}")
print(f"\nO segundo número é par! {resto2==0}")
#--------------------------------------
#------------ Exercicio 6 -------------
numero_neg1 = int(input("\nInsira o primeiro número:"))
numero_neg2 = int(input("\nInsira o segundo número:"))

print(f"\nO primeiro número é negativo! {numero_neg1<0}")
print(f"\nO segundo número é negativo! {numero_neg2<0}")
#--------------------------------------
#------------ Exercicio 7 -------------
numero_media1 = float(input("\nInsira o primeiro número:"))
numero_media2 = float(input("\nInsira o segundo número:"))
numero_media3 = float(input("\nInsira o terceiro número:"))

media = (numero_media1+ numero_media2 + numero_media3)/3

print(f"\nA média dos 3 números é: {media}")
#--------------------------------------
#------------ Exercicio 8 -------------
valor1 = float(input("\nInsira o primeiro número:"))
valor2 = float(input("\nInsira o segundo número:"))

resultado1 = valor1 + 15
resultado2 = valor2 * 3

print(f"\n o número {valor1} mais 15 é igual ao número {valor2} multiplicado por 3! {resultado1==resultado2}")
#--------------------------------------
#------------ Exercicio 9 -------------
dividendo = float(input("\nInsira o dividendo:"))
divisor = float(input("\nInsira o divisor:"))

resultado_divisao = dividendo/divisor
resto_divisao = dividendo%divisor

print(f"\nO resultado da divisão entre {dividendo} e {divisor} é: {resultado_divisao} com o resto de: {resto_divisao}")
#--------------------------------------
#------------ Exercicio 10 ------------
celcius = float(input("\nInsira a temperatura a ser convertida:"))

fahrenheit = (celcius * 1.8) + 32

print(f"\n{celcius} graus celcius são {fahrenheit} graus fahrenheit!")
#--------------------------------------
#------------ Exercicio 11 ------------
peso = float(input("\nInsira seu peso em KG:"))
altura = float(input("\nInsira sua altura em m;"))

imc = peso/(altura*altura)

print(f"\nSeu IMC é: {imc:.2f}")
#--------------------------------------
#------------ Exercicio 12 ------------
numero_ponderado1 = float(input("\nDigite o primeiro número:"))
numero_ponderado2 = float(input("\nDigite o segundo número:"))
numero_ponderado3 = float(input("\nDigite o terceiro número:"))

peso_ponderado1 = float(input("\nDigite o peso do primeiro número:"))
peso_ponderado2 = float(input("\nDigite o peso do segundo número:"))
peso_ponderado3 = float(input("\nDigite o peso do terceiro número:"))

pesos_somados = (numero_ponderado1*peso_ponderado1) + (numero_ponderado2*peso_ponderado2) + (numero_ponderado3*peso_ponderado3)

media_ponderada = pesos_somados/(peso_ponderado1+peso_ponderado2+peso_ponderado3)

print(f"\nA média ponderada é: {media_ponderada:.2f}")

#--------------------------------------
#------------ Exercicio 13 ------------
numero_elevado = int(input("\nDigite um número:"))
expoente = int(input("\nDigite por qual valor ele será elevado:"))

resultado_potencia = numero_elevado**expoente

print(f"\nO número {numero_elevado} elevado a {expoente} é: {resultado_potencia}")
#--------------------------------------
#------------ Desafio 1 ---------------
raiz = int(input("\nInsira o valor que calcularemos a raiz cúbica:"))

raiz_cubica = raiz ** (1/3)

print(f"\nA raiz cúbica de {raiz} é {raiz_cubica}")
#--------------------------------------
#------------ Desafio 2 ---------------
dinheiro_inicial = float(input("\nDigite o valor aplicado inicialmente:"))
juros = float(input("\nDigite a taxa de juros anual:"))
anos = float(input("\nDigite a quantidade de anos:"))

juros_final = juros/100
montante = dinheiro_inicial * (1+juros_final)**anos

print(f"\nO valor final total é de R${montante:.2f}")
