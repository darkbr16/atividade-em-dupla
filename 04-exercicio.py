import os
os.system('cls')
print('=== SEJA BEM VINDO PEQUENO GAFANHOTO ===')
print("=== MUNDO ELETRO - CHECKOUT ===")

valor_produto = float(input("Digite o valor do produto (R$): "))
print("Formas de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - A prazo (em até 6x sem desconto)")
opcao = input("Escolha a opção (1 ou 2): ").strip()

match opcao:
    case "1":
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print("\n--- DETALHES DO PAGAMENTO ---")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print("Forma de Pagamento: À vista")
        print(f"Desconto concedido (10%): R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        
    case "2":
        parcelas = int(input("Digite a quantidade de parcelas (máximo 6): "))
        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas
            print("\n--- DETALHES DO PAGAMENTO ---")
            print(f"Valor original: R$ {valor_produto:.2f}")
            print("Forma de Pagamento: A prazo")
            print(f"Quantidade de parcelas: {parcelas}x")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total a pagar: R$ {valor_produto:.2f}")
        else:
            print("\nErro: O número de parcelas deve ser entre 1 e 6!")
            
    case _:
        print("\nErro: Opção de pagamento inválida!")