def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Não é possível dividir por zero!"
    else:
        return x / y

while True:
    
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha not in ['1', '2', '3', '4', '5']:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        continue

    if escolha == '5':
        print("Obrigado por usar a calculadora. Até mais!")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")
        continue

    if escolha == '1':
        print("Resultado:", adicionar(num1, num2))
    elif escolha == '2':
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif escolha == '4':
        resultado = dividir(num1, num2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Resultado:", resultado)
