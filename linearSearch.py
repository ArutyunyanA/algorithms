def LinearSearch(numbers: list[int], target: int) -> int:
    for elem in range(len(numbers)):
        if numbers[elem] == target:
            return elem
    return None
print(LinearSearch([5, 8, 3, 9, 4, 2, 6, 7], 3))