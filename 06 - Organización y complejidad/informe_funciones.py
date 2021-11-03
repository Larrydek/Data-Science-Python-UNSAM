
#%%
import fileparse
def leer_camion(nombre_archivo_camion):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    return fileparse.parse_csv(nombre_archivo_camion, select = ['nombre','cajones','precio'], types = [str, int, float])
#%%
def leer_precios(nombre_archivo_precios):
    return dict(fileparse.parse_csv(nombre_archivo_precios, types = [str, float], has_headers = False))
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
nombre_archivo_camion = '../Data/camion.csv'
camion = leer_camion(nombre_archivo_camion)

nombre_archivo_precios = '../Data/precios.csv'
precios = leer_precios(nombre_archivo_precios)

informe = hacer_informe(camion, precios)
def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    return informe
        
#print(imprimir_informe(informe))


#%%
#Ejercicio 6.10:
#import fileparse

camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float]) #Por defecto Headers = True
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float])

precios = dict(lista_precios)

#6.11
#print(imprimir_informe(informe))

#%%
#Ejercicio 6.12:
import costo_camion
x = costo_camion.costo_camion('F:/Desktop/Ejercicios/ejercicios_python/Data/fecha_camion.csv')
#print(x)


