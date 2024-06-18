def quicksort(arr, low, high):
    if low < high:
        # Particionamos el array y obtenemos el índice del pivote
        pi = partition(arr, low, high)

        # Ordenamos recursivamente las sublistas
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Seleccionamos el pivote (usamos el último elemento)
    pivot = arr[high]
    i = low - 1  # Índice del elemento más pequeño

    for j in range(low, high):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            i = i + 1
            # Intercambiamos los elementos
            arr[i], arr[j] = arr[j], arr[i]

    # Intercambiamos el pivote con el elemento siguiente al elemento más pequeño
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Ejemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Lista original:", arr)
quicksort(arr, 0, n - 1)
print("Lista ordenada:", arr)
