#EJERCICIO 8.1:
##
    
#IMPORTS:
import datetime

def vida_en_segundos():
    '''
    
    INGRESA TU FECHA DE NACIMIENTO
    Y CALCULA LOS SEGUNDOS QUE PASARON
    HASTA EL DÍA DE HOY

    '''

    ahora = datetime.datetime.now() #DÍA DE HOY
    str_ahora = ahora.strftime('%d/%m/%Y') #Convierte a STRING
    print('Hoy es:', str_ahora)
    
    
    print('Ingrese su fecha de nacimiento con el siguiente formato: DD/MM/YYYY')
    cadena_con_fecha = input() #FECHA DE NACIMIENTO
    
    objeto_fecha = datetime.datetime.strptime(cadena_con_fecha,'%d/%m/%Y') #METE LA FECHA Y DETECTA LOS DÍAS/MES/YEAR EN LA STRING
    str_fecha = objeto_fecha.strftime('%d/%m/%Y')
    print('Su fecha de nacimiento es:', str_fecha)
    
    dias_vividos = ahora - objeto_fecha     #Diferencia
    print(f'Usted vivió un total de: {dias_vividos} días')
    
    segundos_vividos = dias_vividos.total_seconds() #Convierte a segundios
    print(f'Equivale a {segundos_vividos} segundos vividos')
    
    return segundos_vividos

vida_en_segundos()
