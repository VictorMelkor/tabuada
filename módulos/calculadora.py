import os

def titulo():
    os.system('cls')
    print('-'*50)
    print('TABUADA'.center(50))
    print('-'*50) 

def calculadora():
    print('Quer ver a tabuada de qual valor?')
    num = int(input('Digite um número inteiro: '))
    if num < 0:
        print('Utilize apenas números positivos!')
    else:
        os.system('cls')
        titulo()
        print(f'Mostrando a tabuada de {num}:'.center(50))
        for c in range(1,11):
            print(f'{num} x {c} = {num * c}'.center(50))
        print()
        continuar()

def continuar():
    resp = str(input('Deseja verificar a tabuada de outro valor? (S/N) ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Deseja verificar a tabuada de outro valor? (S/N) ')).upper().strip()
    if resp == 'S':
        titulo()
        calculadora()
    if resp == 'N':
        os.system('cls')
        print('Programa finalizado!')
        