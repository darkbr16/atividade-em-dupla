import os
os.system('cls')

print('===== CALCULADORA CREDIFACIO =====')
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Escolha o operador (+, -, * ou /): ").strip()

match operador:
    case "+":
        resultado = num1 + num2
        print(f"\nOperação: {num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"\nOperação: {num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"\nOperação: {num1} * {num2} = {resultado}")
    case "/":
        # Bônus: impedir a divisão por zero
        if num2 == 0:
            print("\nErro: Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"\nOperação: {num1} / {num2} = {resultado}")
    case _:
        # Operador inválido
        print("\nAviso: Operador inválido! Escolha entre +, -, * ou /.")