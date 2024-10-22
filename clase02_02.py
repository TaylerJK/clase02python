# Lista de dispositivos de cómputo
# La lista es mutable porque su contenido se puede cambiar
#                0             1         2            3
dispositivos = ['Impresoras','Escaner','Camara web','Luces']
ventas = [2021,2022,2023,2024]
factura = [1200,5000,6000,4500]
# Tuplas
# La tupla es inmutable porque su contenido no se puede cambiar
#            0         1            2       3
servidor = ('SUNAT','198.23.0.10','Lima','admin')
#reemplazar impresoras por ventilador
dispositivos[0] = 'Ventilador'
print(dispositivos)

# Reemplazar SUNAT por INDECOPI
# servidor[0] = 'INDECOPI'
# print(servidor)