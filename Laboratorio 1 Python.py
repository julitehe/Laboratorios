import numpy as np

# Función para generar el arreglo B
def generar_arreglob(l):
    arrb = np.random.randint(1, 20, l)
    return arrb

tamaño = int(input("Por favor ingresa la longitud del arreglo A: "))
# Ciclo que repite la pregunta si la entrada es menor que 1 o mayor que 12:
while tamaño > 12 or tamaño < 1:
    tamaño = int(input("Inválido, por favor ingresa un número entero entre 1 y 12: "))


# Ciclo que repite la pregunta si la entrada es diferente a la longitud:
while True:
    arr_A = np.array(input("Ingresa todos los números del arreglo, separados con espacio: ").split())
    if len(arr_A) == tamaño:
        break
    else:
        print("Inválido. Revisa que la cantidad de números corresponda con la longitud.")
        arr_A = np.array(input("Ingresa todos los números del arreglo, separados con espacio: ").split())


arr_A = arr_A.astype(np.int64) # Convierte los números ingresados (que ahora mismo son strings) en ints
arr_B = generar_arreglob(tamaño) # Genera el arreglo B llamando a la función generar_arreglob()
print("Arreglo A: ", arr_A)
print("Arreglo B: ", arr_B)

# Suma y multiplicación de A y B
resultado_suma = arr_A + arr_B
resultado_mult = arr_A * arr_B
print("Suma de A y B: ", resultado_suma)
print("Multiplicación de A y B: ", resultado_mult)

# Suma de todos los pares en el arreglo A
pares_arregloA = np.array(arr_A[arr_A % 2 == 0])
suma_de_pares = np.sum(pares_arregloA)
print("Suma de todos los números pares en el arreglo A: ", suma_de_pares)

# Promedio de todos los números en el arreglo B
promedio = round(np.sum(arr_B) / len(arr_B),2)
print("Promedio de todos los números en el arreglo B: ", promedio)

arr_C = np.dstack((arr_A,arr_B)).flatten() # Crea el arreglo C. La función np.dstack() crea pares 'verticales' apilando los dos arreglos.
# Después, la función .flatten() los pasa de pares a una sola línea alternados.
print("Arreglo C: ", arr_C)

valor_max = np.max(arr_C) # Encuentra el máximo valor en C
posicion = np.where(arr_C == valor_max)[0][0] # np.where() devuelve el índice del elemento en el arreglo C que cumple con la condición 

print(f"El valor máximo del arreglo C es {valor_max} en el índice {posicion}.")
