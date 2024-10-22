'''
Ingrese nombre del empleado, horas y minutos travajados y el costo por
hora, para halalr el importe a pagar
'''
# int (integer) entero
# float (flotante) decimal
print('--------------------------------')
print('CALCULO DE HORAS TRABAJADAS')
print('--------------------------------')
xnom = input('Ingrese nombre: ')
xhoras = int(input('Ingrese horas trabajadas: '))
xmin = int(input('Ingrese minutos trabajados: '))
xcosto = float(input('Ingrese el costo por hora: '))

# Calcular
total = xcosto*xhoras + (xcosto/60)*xmin
print('R E S U L T A D O S')
print('Travajador: ', xnom)
print('Horas trabajadas: ',xhoras)
print('Minutos trabajados: ',xmin)
print('Total a pagar es: ',(int(total*100))/100)
