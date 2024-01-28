def sortingAlgorithm(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return sortingAlgorithm(less) + [pivot] + sortingAlgorithm(greater)

if __name__ == '__main__':
    print(sortingAlgorithm([10, 1, 7, 3, 9, 5, 4, 6, 2, 8]))