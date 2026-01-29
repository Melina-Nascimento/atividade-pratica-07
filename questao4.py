import json

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo,'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json   
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")



def escrever_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo,'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        return f"Dados escritos com sucesso no arquivo '{nome_arquivo}'."
    except Exception as e:
        return f"Erro ao escrever no arquivo: {e}"
    
dados = {
    "nome": "Ana Silva",
    "idade": 28,
    "cidade": "Rio de Janeiro",
}

nome = input ("Digite o nome do arquivo JSON: ")
print(escrever_arquivo(nome, dados))
print(ler_arquivo(nome))
