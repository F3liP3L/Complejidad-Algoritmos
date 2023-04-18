def selection_sort(arr):
    n = len(arr)

    # Recorrer todos los elementos del array
    for i in range(n):

        # Encontrar el elemento mínimo restante en el array desordenado
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Intercambiar el elemento mínimo con el primer elemento del array desordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
