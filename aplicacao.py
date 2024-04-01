from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from pesquisa import Pesquisa

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pesquisa de Hábitos de Vida")
        self.pesquisa = Pesquisa()
        self.criar_interface()

    def obter_respostas(self):
        return [resposta.get() for resposta in self.respostas_var]

    def criar_interface(self):
        tk.Label(self, text="Data de Nascimento (DD/MM/AAAA):").grid(row=0, column=0, sticky='w')
        self.data_nascimento_entry = tk.Entry(self)
        self.data_nascimento_entry.grid(row=0, column=1)

        tk.Label(self, text="Gênero:").grid(row=1, column=0, sticky='w')
        self.genero_var = tk.StringVar()
        genero_options = [
            ("Masculino", "Masculino"),
            ("Feminino", "Feminino"),
            ("Não binário", "Não binário"),
            ("Agênero", "Agênero"),
            ("Gênero fluido", "Gênero fluido"),
            ("Bigênero", "Bigênero"),
            ("Transgênero", "Transgênero"),
            ("Intersexo", "Intersexo"),
            ("Outro", "Outro"),
            ("Prefiro não dizer", "Prefiro não dizer")
        ]
        for i, (text, value) in enumerate(genero_options):
            tk.Radiobutton(self, text=text, variable=self.genero_var, value=value).grid(row=i+2, column=0, sticky='w')

        self.respostas_var = []
        for i, pergunta in enumerate(self.pesquisa.perguntas):
            tk.Label(self, text=pergunta).grid(row=i+3+len(genero_options), column=0, sticky='w')
            resposta_var = tk.StringVar(value="")
            self.respostas_var.append(resposta_var)
            tk.Radiobutton(self, text="Sim", variable=resposta_var, value="Sim").grid(row=i+3+len(genero_options), column=1, sticky='w')
            tk.Radiobutton(self, text="Não", variable=resposta_var, value="Não").grid(row=i+3+len(genero_options), column=2, sticky='w')
            tk.Radiobutton(self, text="Não sei responder", variable=resposta_var, value="Não sei responder").grid(row=i+3+len(genero_options), column=3, sticky='w')

        tk.Button(self, text="Salvar", command=self.salvar_pesquisa).grid(row=len(self.pesquisa.perguntas)+4+len(genero_options), columnspan=4)

    def salvar_pesquisa(self):
        data_nascimento_str = self.data_nascimento_entry.get()
        try:
            self.pesquisa.data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
            self.pesquisa.idade = self.pesquisa.calcular_idade(self.pesquisa.data_nascimento)
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato DD/MM/AAAA.")
            return

        self.pesquisa.genero = self.genero_var.get()
        if self.pesquisa.genero == "":
            messagebox.showerror("Erro", "Por favor, selecione um gênero.")
            return

        respostas = self.obter_respostas()
        for resposta in respostas:
            if resposta == "":
                messagebox.showerror("Erro", "Por favor, responda a todas as perguntas.")
                return
        self.pesquisa.respostas = respostas
        self.pesquisa.salvar_respostas()

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
