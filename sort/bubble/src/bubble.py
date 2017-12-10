
def swap(array, a, b):
    temp = array[b]
    array[b] = array[a]
    array[a] = temp

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length):
            if array[i] < array[j]:
                swap(array, i, j)

array = [3, 2, 1, 4, 6, 4, 3, 7, 10, 3, 2]
bubble_sort(array)

print(array)