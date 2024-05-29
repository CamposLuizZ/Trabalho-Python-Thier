import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora de IMC")

        self.rotulo_altura = tk.Label(raiz, text="Altura (m):")
        self.rotulo_altura.pack()
        self.entrada_altura = tk.Entry(raiz)
        self.entrada_altura.pack()

        self.rotulo_peso = tk.Label(raiz, text="Peso (kg):")
        self.rotulo_peso.pack()
        self.entrada_peso = tk.Entry(raiz)
        self.entrada_peso.pack()

        self.botao_calcular = tk.Button(raiz, text="Calcular IMC", command=self.calcular_imc)
        self.botao_calcular.pack()

        self.rotulo_resultado = tk.Label(raiz, text="IMC:")
        self.rotulo_resultado.pack()

    def calcular_imc(self):
        try:
            altura = float(self.entrada_altura.get())
            peso = float(self.entrada_peso.get())
            imc = peso / (altura ** 2)
            self.rotulo_resultado.config(text=f"IMC: {imc:.2f}")
            self.mostrar_categoria_imc(imc)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")

    def mostrar_categoria_imc(self, imc):
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"
        messagebox.showinfo("Categoria do IMC", f"Seu IMC é {imc:.2f} e você está na categoria: {categoria}")

if __name__ == "__main__":
    raiz = tk.Tk()
    app = CalculadoraIMC(raiz)
    raiz.mainloop()
