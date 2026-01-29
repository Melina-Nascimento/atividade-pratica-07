import pandas as pd

def processar_logs_treinamentos(arquivo_log):
    try:
        leitor = pd.read_csv(arquivo_log)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Média: {media:.2f}, desvio padrão: {desvio_padrao:.2f}"

    except FileNotFoundError:
        return "Arquivo de log não encontrado."
    

arquivo = input("Digite o nome do arquivo de log: ")
resultado = processar_logs_treinamentos(arquivo)
print(resultado)
