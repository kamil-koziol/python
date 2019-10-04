lista = ['aaron','bułka','cool']

def Bsearch(arr, num):
    start = 0
    end = len(arr) - 1

    while start <= end:
        half = (start + end)//2
        if num < arr[half]:
            end = half - 1
        elif num > arr[half]:
            start = half + 1
        elif arr[half] == num:
            return half
    return None
        
print(Bsearch(lista, 'aaron'))