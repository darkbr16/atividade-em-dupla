import os
os.system('cls')
soma=0
while True:
    print ('=====BEM VINDO AO RESTAURANTE======')

    print('os pratos disponives no cardapio sao')
    print('codigo     prato      valor   ')
    print('  1       picanha     25.00$  ')
    print('  2       lasanha     20.00$  ')
    print('  3      strogonoff   18.00$  ')
    print('  4    bife acebolado 25.00$  ')
    print('  5     pão com ovo    5.00$  ')

    resposta=input('digite o codigo para selecionar o prato')
    match resposta:
            case 1:
                print('picanha selecionada')
                soma+=25
            case 2:
                print('lasanha selecionada')
                soma+=20
            case 3:
                print('strogonoff selecionado')
                soma+=18
            case 4:
                print('bife acebolado selecionado')
                soma+=25
            case 5:
                print('pao com ovo selecionado')
                soma+=5
            case _:
                print('opçao invalida')
        pergunta=input('gostaria de adicionar outro prato (S|N) ').upper()
    os.system('cls')
    if pergunta==S:
            
