import os
os.system('cls')

print("=== FINANCEIRA CONFIA - PRÉ-ANÁLISE DE CRÉDITO ===")

renda_mensal = float(input("Digite a renda mensal do cliente (R$): "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
num_prestacoes = int(input("Digite a quantidade de prestações: "))

prestacao = valor_emprestimo / num_prestacoes

# Regras para aprovação
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print("\n--- RESULTADO DA ANÁLISE ---")
print(f"Valor da Prestação: R$ {prestacao:.2f}")

if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("Status do Crédito: APROVADO")
else:
    print("Status do Crédito: NEGADO")
    if valor_emprestimo > limite_emprestimo:
        print("- Motivo: O empréstimo excede 10x a renda mensal.")
    if prestacao > limite_prestacao:
        print("- Motivo: A prestação excede 30% da renda mensal.")