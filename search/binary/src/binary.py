
def binary_search_recursive(array, item, left, right):
    """
    Return ``index`` of finded ``item`` in array. 
    If ``item`` not contains in ``array`` return ``-1``
    """
    mid = int((left + right) / 2) # infinite values for integers in python D:

    if array[mid] == item:
        return mid
    elif left == right:
        return -1
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, right) # Фишка с полуинтервалами (см. примечания)
    elif array[mid] > item:
        return binary_search_recursive(array, item, left, mid)

def binary_search(array, item):
    """Wrapper"""
    return binary_search_recursive(array, item, 0, len(array) - 1)

array = [1, 3, 5, 2, 7, 10, 8, 34, 95, 43, 56, 23, 43]
array.sort()

index = binary_search(array, 123)
print(index) # should be 9