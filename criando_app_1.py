import tkinter as tk # Biblioteca para criar interfaces gráficas

janela = tk.Tk() # Criação da janela principal

janela.title("Cotação de Moedas") # Título da janela

# Configuração do tamanho, cor de fundo e cor da letra do texto na janela
mensagem = tk.Label(text="Sistema de busca de cotações de moedas", fg="white", bg="black", width=50, height=1)
mensagem.pack() # Exibe(coloca) dentro da janela

mensagem2 = tk.Label(text="Selecione a moeda desejada:", fg="black", bg="white", width=50, height=1)
mensagem2.pack()

moeda = tk.Entry(width=50) # Campo de caixa de texto para usuário digitar
moeda.pack()

janela.mainloop() # Abre a janela e mantém ela aberta até que seja fechada pelo usuário

