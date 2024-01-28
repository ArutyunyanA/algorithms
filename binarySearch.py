import random

def BinarySearch(array: list[int], target: int) -> int:
    start = 0
    stop = len(array) - 1
    
    while start <= stop:
        mid = (start + stop) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            stop = mid - 1
        else:
            return mid
    return None

print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], random.randint(1, 9)))