import numeros

def inicio():
    while True:
        print('''\nBienvenido, escriba la letra del área a la que desea acceder:
        P - Perfumería
        F - Farmacia
        C - Cosméticos
        T - Terminar''')

        try:
            area = input('Letra: ').upper()
            letras = ['P','F','C','T']
            letras.index(area)

            if area == 'P':
                numeros.decorador(area)
            elif area == 'F':
                numeros.decorador(area)
            elif area == 'C':
                numeros.decorador(area)
            elif area == 'T':
                break

        except:
            print('Opción incorrecta')



inicio()


