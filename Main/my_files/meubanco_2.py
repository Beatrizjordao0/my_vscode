import tkinter as tk
import tkinter.simpledialog as sd
import random

class JogoFinanceiro:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo do Capitalista")
        self.root.attributes('-fullscreen', True)  # Define a janela para tela cheia

        self.dinheiro_banco = 500
        self.dinheiro_comigo = 200
        self.rodada = 1
        self.rodadas_sem_deposito = 0
        self.carros_comprados = []

        self.criar_interface()

    def criar_interface(self):
        # Labels
        self.label_titulo = tk.Label(self.root, text="JOGO DO CAPITALISTA", fg="purple", font=("Arial", 16, "bold"))
        self.label_titulo.pack(pady=10)

        self.label_dinheiro_comigo = tk.Label(self.root, text=f"Saldo com você: {self.dinheiro_comigo} coins", font=("Arial", 12))
        self.label_dinheiro_comigo.pack(pady=5)

        self.label_dinheiro_banco = tk.Label(self.root, text=f"Saldo no banco: {self.dinheiro_banco} coins", font=("Arial", 12))
        self.label_dinheiro_banco.pack(pady=5)

        self.label_rodada = tk.Label(self.root, text=f"Rodada: {self.rodada}", font=("Arial", 15))
        self.label_rodada.pack(pady=5)

        # Botões
        self.botao_trabalhar = tk.Button(self.root, text="Trabalhar", command=self.trabalhar, width=30, font=('Arial', 12))
        self.botao_trabalhar.pack(pady=50)

        self.botao_depositar = tk.Button(self.root, text="Depositar", command=self.depositar, width=30, font=('Arial', 12))
        self.botao_depositar.pack(pady=50)

        self.botao_investir = tk.Button(self.root, text="Investir", command=self.investir, width=30, font=('Arial', 12))
        self.botao_investir.pack(pady=50)

        self.botao_sacar = tk.Button(self.root, text="Sacar", command=self.sacar, width=30, font=('Arial', 12))
        self.botao_sacar.pack(pady=50)

        self.botao_comprar = tk.Button(self.root, text="Comprar", command=self.criar_janela_compra, width=30, font=('Arial', 12))
        self.botao_comprar.pack(pady=20)

        self.botao_sair = tk.Button(self.root, text="Sair", command=self.root.quit, width=30, font=('Arial', 12))
        self.botao_sair.pack(pady=10)

    def trabalhar(self):
        rendimentos = ["péssimo", "ruim", "bom", "ótimo", "excelente"]
        rendimento = random.choice(rendimentos)
        ganhos = {"péssimo": 20, "ruim": 30, "bom": 30, "ótimo": 130, "excelente": 230}

        ganho = ganhos[rendimento]
        self.dinheiro_comigo += ganho
        self.atualizar_labels()
        sd.messagebox.showinfo("Trabalho", f"Seu rendimento foi: {rendimento}\nGanhos: {ganho}")

    def sacar(self):
        quantia = sd.askinteger("Saque", "Quantos coins você quer sacar?")
        if quantia is not None and quantia <= self.dinheiro_banco:
            self.dinheiro_banco -= quantia
            self.dinheiro_comigo += quantia
            self.atualizar_labels()
        elif quantia is not None:
            sd.messagebox.showerror("Erro", "Saldo insuficiente")

    def depositar(self):
        quantia = sd.askinteger("Depósito", "Quantos coins você quer depositar?")
        if quantia is not None and quantia > 0 and quantia <= self.dinheiro_comigo:
            self.dinheiro_comigo -= quantia
            self.dinheiro_banco += quantia
            self.atualizar_labels()
            self.rodadas_sem_deposito = 0
        elif quantia is not None:
            sd.messagebox.showerror("Erro", "Quantidade inválida ou saldo insuficiente!")

    def investir(self):
        quantia = sd.askinteger("Investimento", "Quantos coins você quer investir?")
        if quantia is not None and quantia > 0 and quantia <= self.dinheiro_comigo:
            resultado = random.choice(["ganhou", "perdeu"])
            if resultado == "ganhou":
                ganho = quantia * 2
                self.dinheiro_comigo += ganho
                self.atualizar_labels()
                sd.messagebox.showinfo("Investimento", f"Você ganhou {ganho} coins!")
            else:
                self.dinheiro_comigo -= quantia
                self.atualizar_labels()
                sd.messagebox.showinfo("Investimento", f"Você perdeu {quantia} coins!")
        elif quantia is not None:
            sd.messagebox.showerror("Erro", "Quantidade inválida ou saldo insuficiente!")

    def atualizar_labels(self):
        self.label_dinheiro_comigo.config(text=f"Saldo com você: {self.dinheiro_comigo} coins")
        self.label_dinheiro_banco.config(text=f"Saldo no banco: {self.dinheiro_banco} coins")

        self.rodada += 1
        self.label_rodada.config(text=f"Rodada: {self.rodada}")

        self.rodadas_sem_deposito += 1

        if self.rodada % 5 == 0:
            self.ladrao()

        if len(self.carros_comprados) == 3:
            sd.messagebox.showinfo("Parabéns!", "Você comprou todos os carros! Você ganhou o jogo.")
            self.root.quit()

    def criar_janela_compra(self):
        self.janela_compra = tk.Toplevel(self.root)
        self.janela_compra.title("Loja de Carros")

        self.label_titulo_compra = tk.Label(self.janela_compra, text="Loja de Carros", font=("Arial", 16, "bold"))
        self.label_titulo_compra.pack(pady=10)

        self.label_carro1 = tk.Label(self.janela_compra, text="Carro 1: Palio - Preço: 3000 coins", font=("Arial", 12))
        self.label_carro1.pack(pady=5)
        self.botao_comprar_carro1 = tk.Button(self.janela_compra, text="Comprar Carro 1", command=lambda: self.comprar_carro(1))
        self.botao_comprar_carro1.pack(pady=5)

        self.label_carro2 = tk.Label(self.janela_compra, text="Carro 2: Onix - Preço: 3000 coins", font=("Arial", 12))
        self.label_carro2.pack(pady=5)
        self.botao_comprar_carro2 = tk.Button(self.janela_compra, text="Comprar Carro 2", command=lambda: self.comprar_carro(2))
        self.botao_comprar_carro2.pack(pady=5)

        self.label_carro3 = tk.Label(self.janela_compra, text="Carro 3: Mercedes - Preço: 20000 coins", font=("Arial", 12))
        self.label_carro3.pack(pady=5)
        self.botao_comprar_carro3 = tk.Button(self.janela_compra, text="Comprar Carro 3", command=lambda: self.comprar_carro(3))
        self.botao_comprar_carro3.pack(pady=5)

        self.label_aviso = tk.Label(self.janela_compra, text="", font=("Arial", 12))
        self.label_aviso.pack(pady=5)


    def comprar_carro(self, carro):
        if carro == 1:
            preco = 3000
        elif carro == 2:
            preco = 3000
        elif carro == 3:
            preco = 20000

        if self.dinheiro_comigo >= preco:
            self.dinheiro_comigo -= preco
            self.atualizar_labels()
            self.carros_comprados.append(carro)  # Adiciona o carro à lista de carros comprados
            self.label_aviso.config(text=f"Você comprou o Carro {carro}!")
        else:
            self.label_aviso.config(text="Saldo insuficiente para comprar este carro!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoFinanceiro(root)
    root.mainloop()

