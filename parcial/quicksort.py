
def quicksort(array, pivot):
    if len(array) <= 1:
        return array
    else:
        # Elegir el elemento pivot y dividir el array en sub-arrays menores y mayores
        left = []
        right = []
        for x in array:
            if x <= pivot:
                left.append(x)
            if x > pivot:
                right.append(x)
            # Verificar que los sub-arrays tienen una longitud menor que el array original
        if len(left) < len(array) and len(right) < len(array):
            # Recursivamente ordenar los sub-arrays menores y mayores
            return quicksort(left, pivot) + quicksort(right, pivot)
        else:
            # Si los sub-arrays son iguales al array original, devolver el array original
            return array

print(quicksort([2,8,45,1,500,3,800,9,7],8))