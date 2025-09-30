import tkinter as tk

janela = tk.Tk()

def enviar():
    print(var_aviao.get()) # Como a escolha é uma string(texto), não necessita do if.

var_aviao = tk.StringVar(value="Nada") # Aqui foi criado uma variável sendo string, pq a variável no radionbutton é uma string.

# Criando o RadioButton, passando o texto do botão, a variável a ser atribuída e o valor.
botao_classe_economica = tk.Radiobutton(text="Classe Economica", variable=var_aviao, value="Classe Economica")
botao_classe_executiva = tk.Radiobutton(text="Classe Executiva", variable=var_aviao, value="Classe Executiva")
botao_primeira_classe = tk.Radiobutton(text="Primeira Classe", variable=var_aviao, value="Primeira Classe")

botao_classe_economica.grid(row=0, column=0)
botao_classe_executiva.grid(row=0, column=1)
botao_primeira_classe.grid(row=0, column=2)

botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)



janela.mainloop()