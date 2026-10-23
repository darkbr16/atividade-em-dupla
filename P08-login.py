import os

os.system('cls')


print('=== CADASTRO ===')
cadastro_login = input('Crie um usuario: ')
cadastro_senha = input('Crie uma senha: ')


tentativas = 0

while tentativas < 3:
    print('\n=== LOGIN ===')
    login = input('Digite seu usuario: ')
    senha = input('Digite sua senha: ')

    if login == cadastro_login and senha == cadastro_senha:
        print(f'\nBem-vindo, {cadastro_login}!')
        break  
    else:
        tentativas = tentativas + 1
        print(f'Incorreto! Tentativa {tentativas} de 3.')


if tentativas == 3:
    print('BLOQUEADO FARSANTE')