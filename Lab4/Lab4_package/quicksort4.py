# Defines functions to carry out quicksort of data

swaps = 0
comparisons = 0


def partition(array, low, high):
    """
    Function to partition an array that needs to be sorted
    :param array: array to be sorted
    :param low: starting index
    :param high: ending index
    :return: pivot and pivot index
    """
    global swaps
    global comparisons
    pivot, pivot_index = median_of_three(array, low, high)

    array[low], array[pivot_index] = array[pivot_index], array[low]
    swaps += 1
    index = low + 1

    for item in range(low + 1, high, 1):
        if array[item] < pivot:
            array[index], array[item] = array[item], array[index]
            index += 1
            swaps += 1
            comparisons += 1

    array[low], array[index - 1] = array[index - 1], array[low]
    return index - 1


def median_of_three(_array_, low, high):
    """
    Picks a pivot based on median of three strategy
    :param _array_: array to be sorted
    :param low: starting index
    :param high: ending index
    :return: pivot and pivot index
    """
    global comparisons
    mid = (low + high - 1)//2
    item1 = _array_[low]
    item2 = _array_[mid]
    item3 = _array_[high - 1]

    if item1 <= item2 <= item3:
        comparisons += 1
        return item2, mid
    if item3 <= item2 <= item1:
        comparisons += 1
        return item2, mid
    if item1 <= item3 <= item2:
        comparisons += 1
        return item3, high-1
    if item2 <= item3 <= item1:
        comparisons += 1
        return item3, high-1
    return item1, low


def quick_sort(_array, high, low=0) -> list:
    """
    Function to carry out quick sort
    :param _array: array to be sorted
    :param low: starting index, default param of 0
    :param high: ending index
    :return: sorted list
    """
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * size

    # Initialize top of stack
    top = -1

    # Push initial values of low and high on to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while it's not empty
    while top >= 0:
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at its correct position in sorted array
        pivot = partition(_array, low, high)

        # If there are elements on left side of pivot, then push left side to stack
        if pivot - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1

        # If there are elements on right side of pivot, then push right side to stack
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high

    return _array
