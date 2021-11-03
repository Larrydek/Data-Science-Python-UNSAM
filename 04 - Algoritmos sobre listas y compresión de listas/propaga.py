def propagar(lista):
    
    i = 0    
    while i < len(lista): #da i vueltas para propagar el fuego
        i += 1
        for x, fosforo in enumerate(lista):
            try:
                if fosforo == 0 and lista[x+1] == 1: #si hay 0, 1
                    lista[x] = 1                     #converti el 0 en 1
                elif x > 0 and fosforo == 0 and lista[x-1] == 1: #x > 0 porque sino x podía ser -1 y usaba los elementos de la lista del final
                    lista[x] = 1    #si hay 1, 0, prendé el 0
            except IndexError:      #si hay index error (estas al final de la lista)
                if fosforo == 0 and lista[x-1] == 1: #si hay 1, 0
                        lista[x] = 1                 #prendé el 0
                else: pass
                    
        
    return lista

print(propagar([ 0, 0, 0, 1, 0, 0]))
print(propagar([ 1, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, -1, 0]))
print(propagar([ 0, -1, 1, 0, -1, 0, 0, 1]))