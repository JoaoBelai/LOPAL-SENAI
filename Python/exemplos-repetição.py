ds17 = ['Alex', 'Belai', 'Pedro', 'Samuel']
for menino in ds17:
    print(menino)


mensagem = 'Hello world!'
for caractere in mensagem:
    print(caractere)


cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print(f"Cor: {cor}")


pessoa = {
    "Nome":"Ana",
    "Idade":"30",
    "Profissão":"Programadora"
}
print(pessoa["Nome"])
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


alunos={
    "2024":{
        "nome":"Lucas",
        "idade":17
    },
    "2025":{
        "nome":"Maria",
        "idade":18
    }
}

print(alunos["2025"]["nome"])

for ra, dados in alunos.items():
    print(f"\nRA:{ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")


animais = {"gato", "cachorro", "elefante", 'girafa'}
for animal in animais:
    print(f"Animal: {animal}")

for numero in range(5):
    print(f"{numero}")
print("\n")
for numero in range(1,5):
    print(f"{numero}")
print("\n")
for numero in range(0,11,2):
    print(f"{numero}")
print("\n")
for numero in range(1,11,2):
    print(f"{numero}")
print("\n")



arquivo_texto = "C:/Users/48914771806/Desktop/João Belai/LOP/Python/teste-repeticao.txt"
with open(arquivo_texto, "r", encoding="utf-8")as arquivo:
    for linha in arquivo:
        print(linha.strip())