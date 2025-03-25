# EJERCICIO:

# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


### Operadores aritméticos ###

suma = 3 + 4 # Suma
print(suma) # Imprime la suma

resta = 3 - 4 # Resta
print(resta) # Imprime la resta

multiplica = 3 * 4 # Multiplicación
print(multiplica) # Imprime la multiplicación

divide = 3 / 4 # División
print(divide) # Imprime la división

potencia = 3 ** 4 # Potencia
print(potencia) # Imprime la potencia

modulo = 12 % 5 # Módulo
print(modulo) # Imprime el módulo

division_entera = 12 // 7 # División entera
print(division_entera) # Imprime la división entera

### Operadores de comparación ###

print(3 == 3)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)

### Operadores lógicos ###

print("Ahora veamos otro tipo de operadores")

print(4 == 4 and 4 < 5) 
print(4 == 4 and 4 > 5) 
print(4 == 4 or 4 > 5)
print(4 == 5 or 4 > 5)
print(not 4 == 5)
print(not 5 == 5)

### Operadores de adición ###

my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "Brais"

if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
elif my_string == "Brais":
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev' ni 'Brais'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

### Dificultad extra ###

for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
    elif number == 16:
        print("El número es 16")
    else:
        if number % 2 != 0:
            print(f"{number} es impar")
        else:
            print(f"{number} es múltiplo de 3")


