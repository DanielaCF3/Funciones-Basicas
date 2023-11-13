def cuenta_regresiva(num):
    resultado = []
    for valor in range (num,-1,-1):   
        resultado.append(valor)
    return resultado
print(cuenta_regresiva(10))

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista [1]
devuelve = imprimir_y_devolver([10,20])

def primero_mas_longitud(lista):
    sum = lista[0] + len(lista)
    return sum
print(primero_mas_longitud([1,2,3,4,5]))

def valores_mayores_que_el_segundo(lista):
    if len(lista) > 2:
        return False
    nueva_lista = []
    for valor in lista:
        if valor > lista[1]:
            nueva_lista.append(valor)
    return nueva_lista
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))

def length_and_value(lista):
    lista_nueva = []
    cont = 1
    while cont <= lista[0]:
        lista_nueva.append(lista[1])
        cont += 1
    return lista_nueva
print(length_and_value([4,7]))