import os
import time

os.system('cls')

quantidade = 3
soma = 0

for i in range(quantidade):
    while True:
        nota = float(input(f'Digite sua {i+1}ª nota: '))
        if 0 <= nota <= 10:
            soma += nota
            break
        else:
            print('Nota inválida! Digite um valor entre 0 e 10.')
            time.sleep(1)
            os.system('cls')

media = soma / quantidade

if media >= 7:
    resultado = 'Você foi APROVADO!'
elif media >= 5:
    resultado = 'Você está em RECUPERAÇÃO!'
else:
    resultado = 'Você foi REPROVADO!'

print('\n=== BOLETIM ===')
print(f'Sua média é: {media:.2f}')
print(f'Status: {resultado}')
print(f'Soma total das notas: {soma}')