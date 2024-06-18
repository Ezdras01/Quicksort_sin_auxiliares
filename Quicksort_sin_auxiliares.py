from colorama import Fore, Style, init

# Inicializa colorama
init()

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

def print_colored_list(arr, color):
    colored_list = color + str(arr) + Style.RESET_ALL
    print(colored_list)

# Ejemplo de uso:
arr = [17, 20, 7, 11, 2, 4]
n = len(arr)
print("Lista original:", arr)
print_colored_list(arr, Fore.GREEN)
quicksort(arr, 0, n - 1)
print("Lista ordenada:", arr)
print_colored_list(arr, Fore.RED)
