"""
Ejercicio 3. Programa que compruebe si una variable esta vacia 
y si esta vacia el mismo, relleneralo con texto en minuscula y mostrarlo en 
mayusculas
"""

texto = ""

#metodo strip -> saca los espacios
#metodo len indica longitud 
if len(texto.strip()) <= 0:
    texto = 'soy un texto en minuscula que agregue a la variable vacia'
    print(texto.upper())
else:
    print(f'La variable tiene contenido de texto: {texto}')