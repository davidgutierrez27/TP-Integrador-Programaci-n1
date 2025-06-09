# Función para insertar un valor en un Árbol Binario de Búsqueda
def insertar(arbol, valor):
    if not arbol:
        return [valor, [], []]  # Si el árbol está vacío, se crea un nuevo nodo
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)  # Insertar en el subárbol izquierdo
    else:
        arbol[2] = insertar(arbol[2], valor)  # Insertar en el subárbol derecho
    return arbol


# Función para buscar un valor en el árbol e informar cuántos pasos tomó
def buscar_con_pasos(arbol, valor, pasos=0):
    if not arbol:
        return False, pasos  # Valor no encontrado
    pasos += 1
    if valor == arbol[0]:
        return True, pasos  # Valor encontrado
    elif valor < arbol[0]:
        return buscar_con_pasos(arbol[1], valor, pasos)  # Buscar a la izquierda
    else:
        return buscar_con_pasos(arbol[2], valor, pasos)  # Buscar a la derecha


# Función para mostrar el árbol visualmente con estructura tipo jerárquica -----
def mostrar_arbol(arbol, prefijo="", es_izq=True):
    if arbol:
        # Imprime el nodo actual con líneas según su posición (izquierda o derecha)
        print(prefijo + ("├── "if es_izq else "└── ") + str(arbol[0]))
        if arbol[1] or arbol[2]:  # Si tiene hijos
            # Muestra el hijo izquierdo o (vacio) si no hay
            if arbol[1]:
                mostrar_arbol(arbol[1], prefijo + ("│   " if es_izq else "    "), True)
            else:
                print(prefijo + ("│   " if es_izq else "    ") + "├── (vacio)")
            # Muestra el hijo derecho o (vacio) si no hay
            if arbol[2]:
                mostrar_arbol(arbol[2], prefijo + ("│   " if es_izq else "    "), False)
            else:
                print(prefijo + ("│   " if es_izq else "    ") + "└── (vacio)")


# ---- PROGRAMA PRINCIPAL ----
print("Ingrese números enteros para construir el árbol.")
print("Ingrese 0 para finalizar la carga.\n")
# [20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37]
arbol = []

# Bucle para cargar los valores del árbol
while True:
    try:
        numero = int(input("Ingrese un número (0 para terminar): "))
        if numero == 0:
            break  # Fin de la carga
        arbol = insertar(arbol, numero)  # Se inserta en el árbol
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Búsqueda de un valor en el árbol con conteo de pasos
print("\n Ahora puede buscar un número en el árbol.")
try:
    valor_busqueda = int(input("Ingrese un número a buscar: "))
    encontrado, pasos = buscar_con_pasos(arbol, valor_busqueda)
    if encontrado:
        print(f"El número {valor_busqueda} existe en el árbol. Pasos dados: {pasos}")
    else:
        print(f"El número {valor_busqueda} NO existe en el árbol. Pasos dados: {pasos}")
except ValueError:
    print("Entrada inválida.")

# Muestra el árbol en formato jerárquico
print("\n\n Representación visual del árbol:")
if arbol:
    print(arbol[0])  # Raíz del árbol
    if arbol[1] or arbol[2]:
        if arbol[1]:
            mostrar_arbol(arbol[1], "", True)
        else:
            print("├── (vacio)")
        if arbol[2]:
            mostrar_arbol(arbol[2], "", False)
        else:
            print("└── (vacio)")
