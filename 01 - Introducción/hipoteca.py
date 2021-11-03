# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 17:29:24 2021

@author: Manjuanel
"""

#1.9 calculadora de adelantos
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while mes < pago_extra_mes_comienzo:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print('Total pagado:', total_pagado, saldo)

while mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
    saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
    total_pagado = total_pagado + (pago_mensual + pago_extra)
    mes = mes + 1
    print('Total pagado:', total_pagado, saldo)

    
while saldo > 0 and saldo >= pago_mensual:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    
while saldo < pago_mensual and saldo > 0:
    pago_mensual = saldo
    saldo = 0
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
                
    print('Total pagado:', total_pagado, saldo)

    
    
   
print('Total pagado', round(total_pagado, 2))
print('La deuda fue saldada en', mes, 'meses')
