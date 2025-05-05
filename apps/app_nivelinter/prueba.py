def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])

    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Prueba
arr = [38, 27, 43, 3, 9, 82, 10]
ordenado = merge_sort(arr)
print("Ordenado:", ordenado)



