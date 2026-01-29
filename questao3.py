import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                print(linha)
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

nome_aquivo= input("Digite o nome do arquivo CSV (com extensão .csv):  ")
ler_arquivo_csv(nome_aquivo)
