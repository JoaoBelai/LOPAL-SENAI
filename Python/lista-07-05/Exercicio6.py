def vogais(palavra):
    palavra = palavra.lower()
    lista = ["a", "e", "i", "o", "u"]
    contador = 0
    for letra in range(len(palavra)):
        if palavra[letra] in lista:
            contador += 1

        letra += 1
    return contador

palavra = input("Digite uma palavra: ")

print("Sua palavra tem ", vogais(palavra), " vogais")