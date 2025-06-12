import numpy as np
from datetime import datetime
import random

nombre = input("¿Cómo te llamas? ")

palabras = ['sabiduría', 'gallardía', 'virtud', 'dignidad', 'honor', 'destino', 'misterio', 'gloria']

print("Esto es un archivo de Python tradicional \n")
print(f"La hora actual es {datetime.now()}, {nombre} \n")

while True:
    respuesta = input("¿Te puedo ayudar en algo más? Di solo Sí o No\n")

    while respuesta not in ["Sí", "No"]:
        print("No te entiendo, di solo Sí o No, hasta tú puedes hacerlo\n")
        respuesta = input("¿Te puedo ayudar en algo más? Di solo Sí o No\n")
    
    if respuesta == 'Sí':
        opciones = [
            'Raíz cuadrada, si no es mucha molestia, su altísimo',
            'Palabra aleatoria, por favor mi señor',
            'Nada más, gracias su excelencia'
        ]

        eleccion = None
        while eleccion not in opciones:
            eleccion = input(f"Elige una opción: {opciones}\n")

            if eleccion == 'Raíz cuadrada, si no es mucha molestia, su altísimo':
                try:
                    numero1 = float(input('Dime el número:\n'))
                    print(f"La raíz cuadrada es {np.sqrt(numero1)}\n")
                except ValueError:
                    print("Eso no es un número válido.\n")

            elif eleccion == 'Palabra aleatoria, por favor mi señor':
                print(f"Tu palabra es: {random.choice(palabras)}\n")

            elif eleccion == 'Nada más, gracias su excelencia':
                print("Recuerda quién manda.\n")
                break

            else:
                print(f"Solo conozco estas opciones: {opciones} (recuerda hablarme con propiedad)\n")
    else:
        print("Recuerda quién manda.\n")
        break


        