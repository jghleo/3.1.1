matrix = [['● Número de elementos “amarillo”.', '● Número de elementos “rojo”.'],
          ['● Número de elementos “Naranja”.', '● Número de elementos “Verde”.'],
          ['● Número de elementos “Blanco”.']]
         
import os
os.system("cls")
for row in matrix:
    for element in row:
        print(element)