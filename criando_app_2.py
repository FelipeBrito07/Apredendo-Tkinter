import tkinter as tk # Biblioteca para criar interfaces gráficas
from tkinter import ttk

janela = tk.Tk() # Criação da janela principal

janela.title("Cotação de Moedas") # Título da janela

janela.rowconfigure(0, weight=1) # Configura a linha 0 para expandir automaticamente com "weight=1", o 1 indica que seja automático.
janela.columnconfigure([0, 1], weight=1) # Configura as colunas 0 e 1 para expandir automaticamente.

# Configuração do tamanho, cor de fundo e cor da letra do texto na janela
mensagem = tk.Label(text="Sistema de busca de cotações de moedas", fg="white", bg="black", width=35, height=5)
# Diferente do ".pack()", o ".grid(row= indice, column= indice)" organiza os elementos em linhas e colunas, como se fosse uma grade.
# "columnspan" indica quantas colunas esse texto vai ocupar
# "sticky="NSEW"" indica que o texto deve se expandir para preencher todo o espaço disponível na célular da grade, sendo N = norte, S = Sul, E = Leste e W = Oeste
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW") 

mensagem2 = tk.Label(text="Selecione a moeda desejada:")
mensagem2.grid(row=1, column=0)

# moeda = tk.Entry(width=50) # Campo de caixa de texto para usuário digitar
# moeda.grid(row=1, column=1)

dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000    
}

# Criação de lista suspensa (combobox) para selecionar a moeda
moedas = list(dicionario_cotacoes.keys()) # Obtém as chaves do dicionário de cotações
moeda = ttk.Combobox(janela, values=moedas) # Cria a lista suspensa com as moedas
moeda.grid(row=1, column=1)

# Função que será executada quando o botão for clicado
def buscar_cotacao():
    moeda_preenchida = moeda.get() # O ".get()" obtém o texto digitado na caixa de texto "moeda"
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do {moeda_preenchida} é de R$ {cotacao_moeda} reais."

# Criação do botão que chama a função "buscar_cotação" quando for clicado
botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3 = tk.Label(text="Caso queira pegar mais de uma cotação ao mesmo tempo, digite uma moeda em cada linha.")
mensagem3.grid(row=4, column=0, columnspan=2)   

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky="NSEW")

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n') #Divide o texto em linhas
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f"{item}: {cotacao}")
    mensagem4 = tk.Label(text="\n".join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)

botao_cotacoesmultiplas = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botao_cotacoesmultiplas.grid(row=5, column=1)

janela.mainloop() # Abre a janela e mantém ela aberta até que seja fechada pelo usuário