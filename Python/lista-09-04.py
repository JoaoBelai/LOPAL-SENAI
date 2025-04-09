# #------------ Exercício 1 --------------
# lista = []
# contador = 0
#
# for numero in range (1,11):
#     num = int(input("\nDigite um número: "))
#
#     if num % 3 == 0:
#         print(f"O número {num} é divisível por 3!")
#         lista.append(num)
#         contador += 1
#     else:
#         print(f"O número {num} não é divisível por 3!")
#
# print(f"\nVocê digitou {contador} números divisíveis por 3")
# print(f"\nAqui está a lista completa de números que você digitou que são divisíveis por 3: {lista}")
#
# #---------------------------------------
# #------------ Exercício 2 --------------
#
# senha = "1234"
#
# while True:
#     usuario = input("\nDigite uma senha: ")
#     if usuario == senha:
#         print("\nSenha correta!")
#         break
#     else:
#         print("Senha incorreta!5454 Tente novamente")
#
# #---------------------------------------
# #------------ Exercício 3 --------------
# while True:
#     opcao = int(input("\nTinha o pete e o repete, o pete morreu, quem sobrou?"
#                       "\n1.Pete"
#                       "\n2.Repete"
#                       "\n3.Para, pelo amor de Deus"
#                       "\nEscreva o número da opção: "))
#     if opcao == 3:
#         print("\nBeleza vou parar")
#         break
#
# # ---------------------------------------
# # ------------ Exercício 4 --------------
# num1 = int(input("Digite o número inicial: "))
# num2 = int(input("Digite o número final: "))
# divisor = 2
# lista_primo = []
#
# if num2 < 0 or num1 < 0:
#     print("Números inválidos")
# elif num1 >= num2:
#     print("O primeiro número deve ser menor que o segundo")
# else:
#     for numero in range(num1,num2):
#         divisor = 2
#         while divisor <= numero:
#             resto = numero % divisor
#             if numero == divisor:
#                 lista_primo.append(numero)
#                 break
#             else:
#                 if resto == 0:
#                     break
#                 else:
#                     divisor += 1
#
#     print(f"Os números primos entre {num1} e {num2} são: {lista_primo}")
#
# #---------------------------------------
# #------------ Exercício 5 --------------
#
# senha = "1234"
# chances = 3
# contador = 0
#
# while contador < 3:
#     usuario = input(f"\nDigite a senha de 4 dígitos, você tem {chances} chances: ")
#     if usuario == senha:
#         print("Senha correta!")
#         contador +=3
#     else:
#         print("Senha incorreta")
#         chances -= 1
#         contador += 1
#
# if chances <= 0:
#     print("\nChances zeradas, acesso bloqueado")
#
# # ---------------------------------------
# # ------------ Exercício 6 --------------
# pares = []
# impares = []
#
# for numero in range (1,11):
#     num = int(input("\nDigite um número: "))
#
#     if num % 2 == 0:
#         print(f"O número {num} é par!")
#         pares.append(num)
#     else:
#         print(f"O número {num} é ímpar!")
#         impares.append(num)
#
# print(f"\nAqui está a lista dos números pares que você digitou: {pares}")
# print(f"\nAqui está a lista dos números ímpares que você digitou: {impares}")

# ---------------------------------------
# ------------ Exercício 7 --------------
# frase = input("Digite uma frase: ")
# frase_upp = frase.upper()
# contador = 0
# contador_a = 0
# contador_e = 0
# contador_i = 0
# contador_o = 0
# contador_u = 0
#
# for index in range(0, len(frase_upp)):
#
#     if frase_upp[index] == "A":
#         contador_a += 1
#         contador += 1
#     elif frase_upp[index] == "E":
#         contador_e += 1
#         contador += 1
#     elif frase_upp[index] == "I":
#         contador_i += 1
#         contador += 1
#     elif frase_upp[index] == "O":
#         contador_o += 1
#         contador += 1
#     elif frase_upp[index] == "U":
#         contador_u += 1
#         contador += 1
#
# print(f"\n A sua frase tem {contador} vogais.")
# print(f"\n A sua frase tem {contador_a} letras 'A'.")
# print(f"\n A sua frase tem {contador_e} letras 'E'.")
# print(f"\n A sua frase tem {contador_i} letras 'I'.")
# print(f"\n A sua frase tem {contador_o} letras 'O'.")
# print(f"\n A sua frase tem {contador_u} letras 'U'.")

# ---------------------------------------
# ------------ Exercício 8 --------------
import random
opcoes = ["Cara", "Coroa"]
cont = 0
cont_cara = 0
lista_cara = []

while True:
    while cont < 3:
        escolha = random.choice(opcoes)
        lista_cara.append(escolha)
        cont += 1
        if escolha == "Cara":
            cont_cara += 1
        else:
            cont_cara = 0

    print(lista_cara)
    if cont_cara >= 3:
        break

    cont = 0
    lista_cara = []

# ---------------------------------------
# ------------ Exercício 9 --------------



