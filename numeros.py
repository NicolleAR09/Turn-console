'''
Escribir todos los generadores y el decorador

        print('Su turno es: ')
        funcion(respuesta)
        print('Aguarde y será atendido')
'''


def perfumeria():
    for n in range(1,10000):
        yield f'P - {n}'


def farmacia():
    for n in range(1, 10000):
        yield f'F - {n}'


def cosmeticos():
    for n in range(1, 10000):
        yield f'C - {n}'


p = perfumeria()
f = farmacia()
c = cosmeticos()

def decorador(area):
    print('\nSu turno es: ')
    if area == 'P':
        print(next(p))
    elif area == 'F':
        print(next(f))
    elif area == 'C':
        print(next(c))
    print('Aguarde y será atendido')
