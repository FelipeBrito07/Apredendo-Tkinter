import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())

def atualizar_cotacao():
    moeda = combobox_moeda.get()
    data_cotacao = calendario_data.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_resultado_1['text'] = f'A cotação do {moeda} no dia {data_cotacao} foi de: R${valor_moeda}' 

def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecionar Arquivo de Moeda")
    var_caminho_arquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivo_selecionado['text'] = f"Arquivo Selecionado: {caminho_arquivo}"

def atualizar_cotacoes():
    try:
        # Ler o dataframe de moedas
        df = pd.read_excel(var_caminho_arquivo.get())
        moedas = df.iloc[:, 0]
        # Pegar a data inicial e final
        data_inicial = calendario_data_inicial.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        data_final = calendario_data_final.get()
        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]
        
        # Para cada moeda:
        for moeda in moedas:
            # Pegar todas as cotações da moeda:
            link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/31?' \
                f'start_date={ano_inicial}{mes_inicial}{dia_inicial}&' \
                f'end_date={ano_final}{mes_final}{dia_final}'
            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan
                    
                # Criar uma coluna em um novo dataframe com todas as cotações daquela moeda
                df.loc[df.iloc[:, 0] == moeda, data] = bid 
        # Criar um novo arquivo
        df.to_excel("Teste.xlsx")
        label_resultado_2['text'] = "Arquivo Gerado com Sucesso"
    except:
        label_resultado_2['text'] = "Selecione um Arquivo Excel no Formato Correto"

# Criação da Janela + Título
janela = tk.Tk()
janela.title("Cotação de Moedas")

# # Confuguração da janela:
# janela.configure(bg='white')

# frame = tk.Frame(
#     janela,
#     bg="white",
#     highlightbackground="red",  # cor da borda
#     highlightthickness=20          # espessura da borda
# )
# frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# # Primeira parte, cotação única(Cores e tamanhos que podemos usar: fg="white", bg="black", width=55, height=1):
label_titulo_1 = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid') 
label_titulo_1.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

# Escolher moeda:
label_escolha_moeda = tk.Label(text="Selecione a moeda que deseja consultar:", anchor="e")
label_escolha_moeda.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

combobox_moeda = ttk.Combobox(janela, values=lista_moedas, width=15)
combobox_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

# Escolher data:
label_escolha_data = tk.Label(text="Selecione o dia que deseja consultar:", anchor="e")
label_escolha_data.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

calendario_data = DateEntry(janela, year=2025, locale="pt_br", width=15)
calendario_data.grid(row=2, column=2, padx=10, pady=10, stick='nsew')

# Resultado cotação única moeda:
label_resultado_1 = tk.Label(text="")
label_resultado_1.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

botao_cotacao = tk.Button(text="Cotação", command=atualizar_cotacao, width=14, bg='lightblue')
botao_cotacao.grid(row=3, column=2, padx=10, pady=10)


# # Segunda parte, multiplas cotações:
label_titulo_2 = tk.Label(text="Cotação de 1 moeda específica", borderwidth=2, relief='solid')
label_titulo_2.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

# Selecionar arquivo:
label_escolha_moeda = tk.Label(text="Selecione um arquivo Excel com as Moedas na coluna A:")
label_escolha_moeda.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

var_caminho_arquivo = tk.StringVar()

botao_selecionar_arquivo = tk.Button(text="Selecionar Arquivo", command=selecionar_arquivo, width=14, bg='lightblue')
botao_selecionar_arquivo.grid(row=5, column=2, padx=10, pady=10)

label_arquivo_selecionado = tk.Label(text="Nenhum arquivo selecionado", anchor="w", width=50, wraplength=400)  # quebra de linha automática (em pixels)
label_arquivo_selecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


# Data Inicial
label_escolha_data = tk.Label(text="Data Inicial", anchor='e')
label_escolha_data.grid(row=7, column=0, sticky="nsew", padx=10, pady=10)

calendario_data_inicial = DateEntry(janela, year=2025, locale='pt_br', width=15)
calendario_data_inicial.grid(row=7, column=1, padx=10, pady=10)

# Data final
label_escolha_data = tk.Label(text="Data Final", anchor='e')
label_escolha_data.grid(row=8, column=0, sticky="nsew", padx=10, pady=10)

calendario_data_final = DateEntry(janela, year=2025, locale='pt_br', width=15)
calendario_data_final.grid(row=8, column=1, padx=10, pady=10)

# Botão para atualizar múltiplas cotações:
botao_atualizar_cotacao = tk.Button(text="Atualizar Cotações", command=atualizar_cotacoes, width=20, bg='lightblue')
botao_atualizar_cotacao.grid(row=9, column=0, columnspan=1, padx=10, pady=10, sticky='nsew')

# Resultado múltiplas cotações:
label_resultado_2 = tk.Label(text="")
label_resultado_2.grid(row=9, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)

# Fechar:

botao_fechar = tk.Button(text='Fechar', command=janela.quit, width=15)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')

janela.mainloop()