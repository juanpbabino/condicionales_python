# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

# comienzo del ejercicio

if texto_1 > texto_2:
    print("{}".format(texto_1))
else:
    print("{}".format(texto_2))

if len(texto_1) > len(texto_2):
    print("{}".format(texto_1))
else:
    print("{}".format(texto_2))

if texto_1[0] > texto_2[0]:
    print("{}".format(texto_1))
else:
    print("{}".format(texto_2))

copia_texto_1 = str(input("Ingrese la copia de texto 1:\n"))

if copia_texto_1 == texto_1:
    print("Copia_texto_1 ({}) es igual a texto_1".format(copia_texto_1))
else:
    print("Copia_texto_1 ({}) es distinta de texto_1".format(copia_texto_1))

if copia_texto_1 != texto_2:
    print("Copia_Texto_1({}) es distinta de Texto_2({})".format(texto_1, texto_2))
else:
    print("Copia_Texto_1 ({}) es igual a Texto_2({})".format(texto_1,texto_2))
