# Atividade Prática 07 - Manipulação de Arquivos e Dados (CSV/JSON)

## Descrição

Esta atividade prática faz parte do curso **Escola da Nuvem**. O objetivo desta sétima atividade é capacitar o aluno na **manipulação de arquivos** e persistência de dados. O foco é aprender a ler e escrever informações em formatos estruturados universais, como **CSV** e **JSON**, além de introduzir a análise de dados com a biblioteca **Pandas**.

## Objetivos de Aprendizagem

* Ler e escrever arquivos de texto estruturados (`.csv` e `.json`).
* Utilizar o gerenciador de contexto (`with open`) para manipulação segura de arquivos.
* Serializar dados (transformar dicionários Python em arquivos JSON).
* Realizar análise estatística básica (média e desvio padrão) utilizando **Pandas**.

## Questões Implementadas e Resultados

### Questão 1: Análise de Logs com Pandas
* **Arquivo:** `questao1.py`
* **Descrição:** Programa que utiliza a biblioteca `pandas` para ler um arquivo de log (CSV) contendo tempos de execução. Ele calcula e retorna automaticamente a média e o desvio padrão dos dados.
* **Conceitos:** Biblioteca Pandas (`read_csv`, `.mean()`, `.std()`), tratamento de erro `FileNotFoundError`.
* **Exemplo de Saída:**
    ```text
    Digite o nome do arquivo de log: treinos.csv
    Média: 45.20, desvio padrão: 5.34
    ```

### Questão 2: Escrita de Arquivos CSV
* **Arquivo:** `questao2.py`
* **Descrição:** Script responsável por criar um arquivo CSV a partir de uma lista de dados dentro do código (contendo Nome, Idade e Cidade). Utiliza a biblioteca nativa `csv` para garantir a formatação correta.
* **Conceitos:** Biblioteca `csv`, escrita de arquivos (`writer`, `writerow`), encoding UTF-8.
* **Exemplo de Saída:**
    ```text
    Digite o nome do arquivo CSV: clientes.csv
    Dados escritos com sucesso em clientes.csv
    ```

### Questão 3: Leitura de Arquivos CSV
* **Arquivo:** `questao3.py`
* **Descrição:** Ferramenta para ler o conteúdo de um arquivo CSV existente e exibir suas linhas no terminal. Complementa a questão anterior, permitindo visualizar os dados que foram salvos.
* **Conceitos:** Leitura de arquivos (`reader`), iteração sobre linhas, verificação de existência do arquivo.
* **Exemplo de Saída:**
    ```text
    Digite o nome do arquivo CSV (com extensão .csv):  clientes.csv
    ['Nome', 'Idade', 'Cidade']
    ['Ana', '28', 'São Paulo']
    ['Bruno', '34', 'Rio de Janeiro']
    ['Carla', '22', 'Belo Horizonte']
    ```

### Questão 4: Manipulação de Arquivos JSON
* **Arquivo:** `questao4.py`
* **Descrição:** Programa completo que demonstra o ciclo de vida de um arquivo JSON: primeiro ele escreve um dicionário Python em um arquivo e, em seguida, lê esse mesmo arquivo e exibe os dados formatados.
* **Conceitos:** Biblioteca `json`, serialização (`dump`) e deserialização (`load`), indentação de arquivos.
* **Exemplo de Saída:**
    ```text
    Digite o nome do arquivo JSON: usuario.json
    Dados escritos com sucesso no arquivo 'usuario.json'.
    {'nome': 'Ana Silva', 'idade': 28, 'cidade': 'Rio de Janeiro'}
    ```

## Como Executar os Programas

Para executar qualquer um dos programas Python nesta atividade:
1.  Certifique-se de ter o Python instalado em seu sistema.
2.  **Importante:** Para a questão 1, instale o pandas: `pip install pandas`
3.  Abra um terminal ou prompt de comando.
4.  Navegue até o diretório desta atividade: `cd escoladanuvem/atividadepratica07`
5.  Execute o programa desejado: `python questao1.py` (substitua pelo arquivo correspondente).

