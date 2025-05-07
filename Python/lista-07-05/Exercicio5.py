def primo(num):
    primo = True
    if num == 1:
        primo = False
    else:
        for i in range (2, num):
            resto = num % i
            if resto == 0:
                primo = False

    return primo

valor = int(input("Digite o número que deseja saber se é primo: "))

print("É primo? ", primo(valor))