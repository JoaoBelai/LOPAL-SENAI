import random
import customtkinter as ctk

numeros = [
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15",
    "I16", "I17", "I18", "I19", "I20", "I21", "I22", "I23", "I24", "I25", "I26", "I27", "I28", "I29", "I30",
    "N31", "N32", "N33", "N34", "N35", "N36", "N37", "N38", "N39", "N40", "N41", "N42", "N43", "N44", "N45",
    "G46", "G47", "G48", "G49", "G50", "G51", "G52", "G53", "G54", "G55", "G56", "G57", "G58", "G59", "G60",
    "O61", "O62", "O63", "O64", "O65", "O66", "O67", "O68", "O69", "O70", "O71", "O72", "O73", "O74", "O75"
]

sorteados = []

def sair():
    app.destroy()

def sorteio():
    if len(sorteados) == 75:
        app.destroy()

    numero = random.choice(numeros)
    while numero in sorteados:
        numero = random.choice(numeros)

    sorteados.append(numero)
    numero_sort.configure(text=f'Número sorteado agora:\n {numero}')

    lista_texto = ""
    for i in range(0, len(sorteados), 9):
        lista_texto += ",  ".join(sorteados[i:i + 9]) + "\n"

    lista.configure(text=f'Números Sorteados:\n\n {lista_texto}\n')


ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Bingo')
app.geometry('600x700')

texto = ctk.CTkLabel(app, text='Bingo!', font=ctk.CTkFont(family="Inter" ,size=30, weight='bold'))
texto.pack(pady=30)

sortear = ctk.CTkButton(app, text='Sortear!', command=sorteio, fg_color='green', hover_color='dark green', font=ctk.CTkFont(family="Inter" ,size=20, weight='bold'), width=200, height=40)
sortear.pack(pady=20)

sair = ctk.CTkButton(app, text='Sair', fg_color='red', command=sair, hover_color='dark red', font=ctk.CTkFont(family="Inter" ,size=20, weight='bold'), width=150, height=30)
sair.pack(pady=20)

numero_sort = ctk.CTkLabel(app, text='', font=ctk.CTkFont(family="Inter" ,size=25, weight='bold'))
numero_sort.pack(pady=20)

lista = ctk.CTkLabel(app, text='', font=ctk.CTkFont(family="Inter" ,size=20))
lista.pack(pady=20)

app.mainloop()