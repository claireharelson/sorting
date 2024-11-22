# Defines functions to carry out quicksort of data

swaps = 0
comparisons = 0


def partition(array, low, high) -> int:
    """
    Function to partition an array that needs to be sorted
    :param array: array to be sorted
    :param low: starting index
    :param high: ending index
    :return: partition index
    """
    global comparisons
    global swaps

    index = (low - 1)
    to_compare = array[high]

    for item in range(low, high):
        if array[item] <= to_compare:
            comparisons += 1
            index = index + 1
            array[index], array[item] = array[item], array[index]
        else:
            comparisons += 1
            swaps += 1

    array[index + 1], array[high] = array[high], array[index + 1]
    return index + 1


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
