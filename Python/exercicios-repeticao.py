#-------- Exemplo 1 ---------
print("\nExemplo 1")
for numero in range(0,11,2):
    print(numero)

#----------------------------
#-------- Exemplo 2 ---------
print("\nExemplo 2")
cores = ["Vermelho", "Azul", "Verde", "Amarelo"]

for cor in cores:
    print(f"Cor: {cor}")

#----------------------------
#-------- Exemplo 3 ---------
print("\nExemplo 3")
soma = 0
for numero in range (1,101):
    soma = soma +numero
print(soma)
#----------------------------
#-------- Exemplo 4 ---------
print("\nExemplo 4")
numero = int(input("Digite um número que você gostaria de saber a tabuada: "))

for tabuada in range(0,11):
    resultado = numero*tabuada
    print(f"{numero}X{tabuada} = {resultado}")

#----------------------------
#-------- Exemplo 5 ---------
print("\nExemplo 5")
tamanho = int(input("Digite a quantidade de números que você quer tirar a média:"))
lista = []
sum = 0
for quant in range(0,tamanho):
    nota = float(input(f"Digite a {quant+1}° nota: "))
    lista.append(nota)
    sum = sum + nota

media = sum/tamanho
print(f"\nNúmeros selecionados: {lista}")
print(f"\nA média é: {media}")

#----------------------------
#-------- Exemplo 6 ---------
print("\nExemplo 6")