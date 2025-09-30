import tkinter as tk
import pandas as pd
from tkinter.filedialog import askopenfilename

# Cria a janela
janela = tk.Tk() 

# Configurações de tamanho.
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

# Cria o título da janela
janela.title("Gerador de Joins") 

mensagem = tk.Label(text="Aplicativo para selecionar arquivos Excel e junta-los.")
mensagem.grid(row=0, column=0, columnspan=2)

mensagem2 = tk.Label(text="Você pode selecionar até 2 arquivos xlsx e junta-los como se fosse um join.")
mensagem2.grid(row=1, column=0, columnspan=2)

def escolha1():
    caminho = askopenfilename(title="Selecione o arquivo")
    df = pd.read_excel(caminho)
    print(df)


primeiro_botao = tk.Button(text="Selecione o primeiro arquivo", command=escolha1)
primeiro_botao.grid(row=3, column=0)

segundo_botao = tk.Button(text="Selecione o segundo arquivo", command=escolha1)
segundo_botao.grid(row=3, column=1)


janela.mainloop()