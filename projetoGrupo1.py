import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

def validar_resposta(resposta):
    # Verifica se a resposta contém apenas números 1, 2 ou 3
    if resposta not in ['1', '2', '3']:
        return False
    return True
def validar_resposta1(resposta):
    # Verifica se a resposta contém apenas números 1, 2 ou 3
    if resposta not in ['1', '2', '3','4','5','6','7','8','9','10']:
        return False
    return True

def validar_idade(idade):
    # Verifica se a idade está entre 0 e 120
    try:
        idade = int(idade)
        if idade < 0 or idade > 120:
            return False
    except ValueError:
        return False
    return True

def realizar_pesquisa():
    # Define as perguntas da pesquisa
    perguntas = [
        "Você pratica atividade física regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você consome pelo menos 5 porções de frutas e vegetais por dia? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você costuma dormir pelo menos 7 horas por noite? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>",
        "Você fuma atualmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>>"
    ]
    
    # Verifica se o arquivo já existe e está vazio
    if not os.path.exists('dados_pesquisa.csv') or os.path.getsize('dados_pesquisa.csv') == 0:
        with open('dados_pesquisa.csv', 'w', newline='') as arquivo_csv:
            # Abre o arquivo CSV para escrita
            escritor_csv = csv.writer(arquivo_csv)

            # Escreve o cabeçalho do arquivo CSV
            escritor_csv.writerow(
                ['Idade', 'Genero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Data', 'Hora'])

    # Abre o arquivo CSV para adição
    with open('dados_pesquisa.csv', 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Loop para inserção contínua de respostas
        while True:
            idade = None
            while idade is None or not validar_idade(idade):
                idade = simpledialog.askstring("Idade", "Informe a sua idade:")
                if idade is None:
                    return
                if not validar_idade(idade):
                    messagebox.showerror("Erro", "Por favor, insira uma idade válida entre 0 e 120 anos.")

            genero = None
            while genero is None or not validar_resposta1(genero):
                genero = simpledialog.askstring("Gênero", "Qual o seu gênero?\n1- Masculino\n2- Feminino\n3- Não binário\n4- Agênero\n5- Gênero fluido\n6- Bigênero\n7- Transgênero\n8- Intersexo\n9- Outro\n10- Prefiro não dizer")
                if genero is None:
                    return
                if not validar_resposta1(genero):
                    messagebox.showerror("Erro", "Por favor, insira um gênero válido.")

            respostas = []
            for pergunta in perguntas:
                resposta = None
                while resposta is None or not validar_resposta(resposta):
                    resposta = simpledialog.askstring("Pergunta", pergunta)
                    if resposta is None:
                        return
                    if not validar_resposta(resposta):
                        messagebox.showerror("Erro", "Por favor, insira uma resposta válida.")
                respostas.append(resposta)

            # Obtém data e hora atual
            data_atual = datetime.now().strftime('%Y-%m-%d')
            hora_atual = datetime.now().strftime('%H:%M:%S')

            # Escreve os dados no arquivo CSV
            escritor_csv.writerow([idade, genero] + respostas + [data_atual, hora_atual])

            resposta_continuar = messagebox.askyesno("Continuar?", "Deseja continuar e inserir outro cadastro?")
            if not resposta_continuar:
                messagebox.showinfo("Sucesso", "Dados salvos com sucesso no arquivo 'dados_pesquisa.csv'!")
                break

# Cria uma janela principal
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

# Chama a função para realizar a pesquisa
realizar_pesquisa()
