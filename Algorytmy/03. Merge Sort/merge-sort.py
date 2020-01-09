import random
lista = [random.randint(0,10) for i in range(8)]

print(lista)
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Rekursywne wywołanie na połówkach
        mergeSort(left)
        mergeSort(right)

        # 2 Iteratory dla dwóch połówek
        i = 0
        j = 0
        
        # Iterator dla głównej
        k = 0
        print("LEFT",left)
        print("RIGHT", right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1


        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
        print(myList)

mergeSort(lista)
print(lista)
