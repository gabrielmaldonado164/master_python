#Importo modulos para trabajaro con las fechas

import  datetime

#mostra fecha
print(datetime.date.today())#solo dia, lo muestra: año - mes - dia

print("---------------------------------------------------")

fecha_completa = datetime.datetime.now()#dia y hora 
print(fecha_completa)#Lo muestra: año - mes - dia

print("---------------------------------------------------")

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)


print("---------------------------------------------------")

"""
%d -> dia 
%m -> mes
%Y -> anio

%H -> hora
%M -> minutos
%S -> segundos
"""
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")#formateo la fecha para mostrarlo como quiera yo
print(fecha_personalizada)

print("---------------------------------------------------")

print(datetime.datetime.now().time()) #muestra el tiempo
print(datetime.datetime.now().timestamp()) #tiempo en unix

