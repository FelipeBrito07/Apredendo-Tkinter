from tkinter.filedialog import askopenfilename # Biblioteca do tkinter que abre uma janela para selecionar arquivo.
import pandas as pd

caminho_arquivo = askopenfilename(title="Selecione o arquivo") # Ela traz o caminho do arquivo selecionado.

df = pd.read_excel(caminho_arquivo) # Ai pode usar com o pandas para ler o arquivo do caminho

print(caminho_arquivo)
print(df)