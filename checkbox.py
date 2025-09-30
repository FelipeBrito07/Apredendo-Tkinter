import tkinter as tk

janela = tk.Tk() # Criando a janela principal(interface)


var_promocoes = tk.IntVar() # Variável associada ao checkbox (0 - desmarcado, 1 - marcado)
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocionais?", variable=var_promocoes) # Criação do checkbox
# Variable armazena a resposta da marcação do checkbox.
checkbox_promocoes.grid(row=0, column=0) # Insere o checkbox na janela.


var_termo_de_uso = tk.IntVar()
checkbox_termo_de_uso = tk.Checkbutton(text="Aceito os termos de uso.", variable=var_termo_de_uso)
checkbox_termo_de_uso.grid(row=1, column=0)


def enviar():
    promo = var_promocoes.get()
    termos = var_termo_de_uso.get()

    if not termos:
        print("Para seguir, você deve aceitar os termos de uso da plataforma.")
    elif promo:
        print("Você aceitou os termos de uso e receberá e-mails promocionais.")
    else:
        print("Você aceitou os termos de uso e optou por não receber e-mails promocionais.")
    

botao_enviar = tk.Button(text="Enviar", command=enviar) # Criação do botão para enviar a resposta.
botao_enviar.grid(row=2, column=0)

janela.mainloop()