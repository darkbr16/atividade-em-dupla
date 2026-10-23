import os
os.system('cls')

quantidade=5
contadorpar=0
contadorimpar=0
soma=0
for i in range(quantidade):

    numero=int(input(f'digite o seu {i+1}º numero:  '))
    soma+=numero
    if numero%2==0:
        contadorpar+=1
    else:
        contadorimpar+=1

print('\n===RESULTADO===')

print(f'numero de pares {contadorpar} ')
print(f'numero de impares {contadorimpar} ')
print(f'a soma de todos os numeros e {soma}')