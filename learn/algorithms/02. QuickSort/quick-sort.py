import random
lista = [random.randint(0,1000) for i in range(500)]

def quick_sort(array):

    mniejsze = []
    rowne = []
    wieksze = []

    if len(array) > 1: # chcemy sprawdzać tylko gdy jest więcej niż 1 element w liście
        pivot = array[0]
        for x in array:
            if x < pivot:
                mniejsze.append(x)
            elif x == pivot:
                rowne.append(x)
            elif x > pivot:
                wieksze.append(x)

        return quick_sort(mniejsze) + rowne + quick_sort(wieksze)
    else: 
        return array

print(quick_sort(lista))