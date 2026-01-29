import csv

def escrever_csv(nome_arquivo,dados):
    
    try:
        with open(nome_arquivo,'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(['Nome', 'Idade', 'Cidade']) 
            for linha in dados:
                escritor_csv.writerow(linha)
            return f"Dados escritos com sucesso em {nome_arquivo}"
        


    except Exception as e:
        return f"Ocorreu um erro ao escrever o arquivo: {e}"
    
dados = [
    ['Ana', 28, 'São Paulo'],
    ['Bruno', 34, 'Rio de Janeiro'],
    ['Carla', 22, 'Belo Horizonte']
]


nome_arquivo = input("Digite o nome do arquivo CSV:")
print(escrever_csv(nome_arquivo,dados))
