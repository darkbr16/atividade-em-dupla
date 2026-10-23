import os
os.system('cls')

# ex02_desconto_atacado.py

print("=== ATACAREJO BOM PREÇO - CAIXA ===")

produto = input("Nome do produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário (R$): "))

total_bruto = quantidade * preco_unitario

# Regra de descontos
if quantidade <= 5:
    percentual_desconto = 0.02  # 2%
elif quantidade <= 10:
    percentual_desconto = 0.03  # 3%
else:
    percentual_desconto = 0.05  # 5%

valor_desconto = total_bruto * percentual_desconto
total_a_pagar = total_bruto - valor_desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Produto: {produto}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")