#import csv
#import fileparse
#%%
import fileparse
def leer_camion(nombre_archivo_camion):
    '''
    LEE UN ARCHIVO Y ORDENA LOS DATOS DE CADA FRUTA
    
    PRE: DEBE INGRESAR LA RUTA DE UN ARCHIVO LEGIBLE
    POS: DEVUELVE UNA LISTA DE DICCIONARIOS CON LOS DATOS SELECCIONADOS
    '''
    with open(nombre_archivo_camion) as file:
        return fileparse.parse_csv(file, select = ['nombre','cajones','precio'], types = [str, int, float])

#nombre_archivo_camion = '../Data/camion.csv'
#camion = leer_camion(nombre_archivo_camion)

print('-------------------------------------------')
#print(camion)

#%%
def leer_precios(nombre_archivo_precios):
    '''
    LEE UN ARCHIVO, LO ABRE Y
   ORDENA EN UN DICCIONARIO {KEY: VALUE}
   LAS FRUTAS CON SU DATOS
    '''
    with open(nombre_archivo_precios) as file:
        return dict(fileparse.parse_csv(file, types = [str, float], has_headers = False, silence_errors = False))


#nombre_archivo_precios = '../Data/precios.csv'
#precios = leer_precios(nombre_archivo_precios)
print('-------------------------------------------')
#print(precios)
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista
#%%

def imprimir_informe(camion, precios):
    '''
    TOMA DOS ARCHIVOS
    MUESTRA UN INFORME ORDENADO
    COMBINANDO LA LECTURA DE 2 ARCHIVOS
    '''
    
    informe = hacer_informe(camion, precios)
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    print('---------- ---------- ---------- ----------')
    return informe
        
def f_principal(argv):
    if len(argv)!= 3:
        print('Uso inadecuado.')
        print(f'el uso correcto de {argv[0]} es con 2 argumentos más')
    else:
        camion = argv[1]
        precios = argv[2]
        informe = hacer_informe(camion, precios)
        imprimir_informe(informe)

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    
#camion = leer_camion(nombre_archivo_camion)
#precios = leer_precios(nombre_archivo_precios)
#imprimir_informe(camion, precios)


#%%
#Ejercicio 6.10:
#import fileparse

#camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float]) #Por defecto Headers = True
#lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float])

#precios = dict(lista_precios)

#6.11
#print(imprimir_informe(informe))

#%%
#Ejercicio 6.12:
#import costo_camion
#x = costo_camion.costo_camion('F:/Desktop/Ejercicios/ejercicios_python/Data/fecha_camion.csv')
#print(x)





